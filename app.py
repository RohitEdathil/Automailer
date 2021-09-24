"""Integrates all the components and provides a command line interface to the app"""
import click
from json import load, dump
from lib.mail_client import MailClient
from lib.renderer import TemplateRenderer
from lib.parser import parse
from os.path import join


@click.group()
def app():
    """Utility to send bulk personalized emails"""
    pass


@app.command()
@click.option("--email", prompt="Enter email id", help="Email ID of sender")
@click.option("--pwd", prompt="Enter password", help="Password of sender", hide_input=True)
def config(email, pwd):
    """Configures the app"""
    try:
        MailClient(email, pwd)
        # Writes the email and password to config.json
        with open('config.json', 'w') as f:
            dump({'email': email, 'pwd': pwd}, f)
        click.echo(f'Automailer configured successfully')
    except Exception as e:
        # Prints error if failed to login
        click.echo(f'Error: {e}')


@app.command()
@click.argument("job")
@click.option("--data-file", default='', type=click.Path(), help="Use a file other than jobs/job/data.csv as data source")
def run(job, data_file):
    """Sends email using info from said 'job' folder"""
    click.echo(f'Starting {job} ... ')
    try:
        try:
            config = load(open("config.json", "r"))
        except FileNotFoundError:
            return click.echo(f'Error: Configure the app first')
        # Logs in to smtp server
        mail_client = MailClient(config['email'], config['pwd'])
        click.echo(f"Logged in as {config['email']}")
        # Loads template
        template_path = join('jobs', job, 'template.html')
        renderer = TemplateRenderer(template_path)
        click.echo(f"Loaded template from {template_path}")
        # Loads data
        csv_path = join(
            'jobs', job, 'data.csv') if data_file == '' else data_file
        click.echo(f"Loaded data from {csv_path}")

        # Processes data and send emails
        headers, data = parse(csv_path)
        for row in data:
            email_data = dict(zip(headers, row))
            content = renderer.render(email_data)
            mail_client.send(email_data['email'],
                             email_data['subject'], content)
    except Exception as e:
        click.echo(f'Error: {e}')
        return


if __name__ == '__main__':
    app()
