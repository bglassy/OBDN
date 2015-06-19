#!/usr/bin/env python
# coding: utf-8

import logging
import click

from obdocs import __version__
from obdocs import build
from obdocs import serve
from obdocs import utils
from obdocs import exceptions
from obdocs.config import load_config

log = logging.getLogger(__name__)


class State(object):
    ''' Maintain logging level.'''

    def __init__(self, log_name='obdocs', level=logging.INFO):
        self.logger = logging.getLogger(log_name)
        self.logger.propagate = False
        stream = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)-7s -  %(message)s ")
        stream.setFormatter(formatter)
        self.logger.addHandler(stream)

        self.logger.setLevel(level)


pass_state = click.make_pass_decorator(State, ensure=True)


def verbose_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        if value:
            state.logger.setLevel(logging.DEBUG)
    return click.option('-v', '--verbose',
                        is_flag=True,
                        expose_value=False,
                        help='Enable verbose output',
                        callback=callback)(f)


def quiet_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        if value:
            state.logger.setLevel(logging.ERROR)
    return click.option('-q', '--quiet',
                        is_flag=True,
                        expose_value=False,
                        help='Silence warnings',
                        callback=callback)(f)


def common_options(f):
    f = verbose_option(f)
    f = quiet_option(f)
    return f


clean_help = "Remove old files from the site_dir before building"
config_file_help = "Provide a specific obdocs config"
dev_addr_help = ("IP address and port to serve documentation locally (default: "
                 "localhost:8000)")
strict_help = ("Enable strict mode. This will cause obdocs to abort the build "
               "on any warnings.")
theme_help = "The theme to use when building your documentation."
theme_choices = utils.get_theme_names()
site_dir_help = "The directory to output the result of the documentation build."
reload_help = "Enable and disable the live reloading in the development server."
commit_message_help = ("A commit message to use when commiting to the "
                       "Github Pages remote branch")
remote_branch_help = ("The remote branch to commit to for Github Pages. This "
                      "overrides the value specified in config")


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '-V', '--version')
@common_options
def cli():
    """
    OBDocs - OpenBazaar Platform Documentation
    """
    pass


@cli.command(name="serve")
@click.option('-f', '--config-file', type=click.File('rb'), help=config_file_help)
@click.option('-a', '--dev-addr', help=dev_addr_help, metavar='<IP:PORT>')
@click.option('-s', '--strict', is_flag=True, help=strict_help)
@click.option('-t', '--theme', type=click.Choice(theme_choices), help=theme_help)
@click.option('--livereload/--no-livereload', default=True, help=reload_help)
@common_options
def serve_command(dev_addr, config_file, strict, theme, livereload):
    """Run the builtin development server"""

    logging.getLogger('tornado').setLevel(logging.WARNING)

    try:
        serve.serve(
            config_file=config_file,
            dev_addr=dev_addr,
            strict=strict,
            theme=theme,
            livereload=livereload,
        )
    except exceptions.ConfigurationError as e:
        # Avoid ugly, unhelpful traceback
        raise SystemExit('\n' + str(e))


@cli.command(name="build")
@click.option('-c', '--clean', is_flag=True, help=clean_help)
@click.option('-f', '--config-file', type=click.File('rb'), help=config_file_help)
@click.option('-s', '--strict', is_flag=True, help=strict_help)
@click.option('-t', '--theme', type=click.Choice(theme_choices), help=theme_help)
@click.option('-d', '--site-dir', type=click.Path(), help=site_dir_help)
@common_options
def build_command(clean, config_file, strict, theme, site_dir):
    """Build the OBDocs documentation"""
    try:
        build.build(load_config(
            config_file=config_file,
            strict=strict,
            theme=theme,
            site_dir=site_dir
        ), clean_site_dir=clean)
    except exceptions.ConfigurationError as e:
        # Avoid ugly, unhelpful traceback
        raise SystemExit('\n' + str(e))


@cli.command(name="json")
@click.option('-c', '--clean', is_flag=True, help=clean_help)
@click.option('-f', '--config-file', type=click.File('rb'), help=config_file_help)
@click.option('-s', '--strict', is_flag=True, help=strict_help)
@click.option('-d', '--site-dir', type=click.Path(), help=site_dir_help)
@common_options
def json_command(clean, config_file, strict, site_dir):
    """Build to JSON"""

    try:
        build.build(load_config(
            config_file=config_file,
            strict=strict,
            site_dir=site_dir
        ), dump_json=True, clean_site_dir=clean)
    except exceptions.ConfigurationError as e:
        # Avoid ugly, unhelpful traceback
        raise SystemExit('\n' + str(e))