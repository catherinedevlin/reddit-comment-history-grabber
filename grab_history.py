#!/usr/bin/env python
# coding: utf-8

import praw
import click

from helpers import get_config


def get_reddit(config):
    user_agent = "{platform}:{qualified_name}:v{version} (by /u/{author})".format(
        **config["REDDIT"]
    )
    credentials = dict(
        client_id=config["REDDIT"]["client_id"],
        client_secret=config["REDDIT"]["client_secret"],
        user_agent=user_agent,
    )
    reddit = praw.Reddit(**credentials)
    return reddit


def quoted(txt):
    return "\n".join("> %s" % line for line in txt.splitlines())


def posted(username, limit):
    config = get_config()
    reddit = get_reddit(config)
    subreddit = config["REDDIT"]["subreddit"].lower()
    user = reddit.redditor(username)
    yield "/u/%s" % username
    for subm in user.submissions.new(limit=10):
        if subm.subreddit.display_name.lower() == subreddit:
            yield "\n\n".join((subm.url, quoted(subm.title), quoted(subm.selftext)))
    for comm in user.comments.new(limit=limit):
        if comm.subreddit.display_name.lower() == subreddit:
            yield ("\n\n").join((comm.link_permalink, quoted(comm.body)))


@click.command()
@click.argument("username")
@click.option("-l", "--limit", help="max number of comments", default=50)
def main(username, limit):
    result = "\n\n\n".join(posted(username, limit))
    click.echo(result)


if __name__ == "__main__":
    main()
