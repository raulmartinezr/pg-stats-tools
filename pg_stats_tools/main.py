"""Main entry for typer CLI"""
import typer
from dotenv import load_dotenv

from pg_stats_tools.pg.cli import pg
from pg_stats_tools.pg.stats.cli import stats
from pg_stats_tools.pg.stats.sql.cli import sql
from pg_stats_tools.pg.stats.indexes.cli import indexes
from pg_stats_tools.pg.stats.buffers.cli import buffers

load_dotenv()
# print(os.environ)

app: typer.Typer = typer.Typer(
    help="""Welcome to AWS Pertformance Insights Reports cli tool
    """,
    rich_markup_mode="rich",
)

app.add_typer(pg, name="pg")
pg.add_typer(stats, name="stats")
stats.add_typer(sql, name="sql")
stats.add_typer(indexes, name="indexes")
stats.add_typer(buffers, name="buffers")

if __name__ == "__main__":
    app()
