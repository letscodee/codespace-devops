import click
import glob

@click.command()
@click.option(
  "--path", prompt = "Path to search for csv files", help = "This is path search for files"
)

@click.option(
  "--ftype", prompt = "Pass in the type of file you want to search", help = "This is path search for files"
)

def search(path, ftype):
  res = glob.glob(f"{path}/*.{ftype}")
  click.echo(click.style("Found Matches", fg="red")
  for result in res:
      click.echo(click.style(f"{result}", fg="white", bg="yellow"
  
