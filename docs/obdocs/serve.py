import logging
import shutil
import tempfile

from obdocs.build import build
from obdocs.config import load_config

log = logging.getLogger(__name__)


def _livereload(host, port, config, builder, site_dir):

    from livereload import Server

    server = Server()

    # Watch the documentation files, the config file and the theme files.
    server.watch(config['docs_dir'], builder)
    server.watch(config['config_file_path'], builder)

    for d in config['theme_dir']:
        server.watch(d, builder)

    server.serve(root=site_dir, host=host, port=int(port), restart_delay=0)


def _static_server(host, port, site_dir):

    # Importing here to seperate the code paths from the --livereload
    # alternative.
    from tornado import ioloop
    from tornado import web

    application = web.Application([
        (r"/(.*)", web.StaticFileHandler, {
            "path": site_dir,
            "default_filename": "index.html"
        }),
    ])
    application.listen(port=port, address=host)

    log.info('Running at: http://%s:%s/', host, port)
    log.info('Hold ctrl+c to quit.')
    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        log.info('Stopping server...')


def serve(config_file=None, dev_addr=None, strict=None, theme=None,
          livereload=True):
  
    # Create a temporary build directory, and set some options to serve it
    tempdir = tempfile.mkdtemp()

    def builder():
        log.info("Building documentation...")
        config = load_config(
            config_file=config_file,
            dev_addr=dev_addr,
            strict=strict,
            theme=theme,
        )
        config['site_dir'] = tempdir
        build(config, live_server=True)
        return config

    # Perform the initial build
    config = builder()

    host, port = config['dev_addr'].split(':', 1)

    try:
        if livereload:
            _livereload(host, port, config, builder, tempdir)
        else:
            _static_server(host, port, tempdir)
    finally:
        shutil.rmtree(tempdir)
