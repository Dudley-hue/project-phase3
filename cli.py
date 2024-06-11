import click
from models import Base, engine, Session, City, Weather, Forecast
from datetime import date, datetime

@click.group()
def cli():
    pass

@click.command()
def initdb():
    """Initialize the database."""
    Base.metadata.create_all(engine)
    click.echo("Initialized the database")

@click.command()
@click.argument('name')
def add_city(name):
    """Add a new city."""
    session = Session()
    if session.query(City).filter_by(name=name).first():
        click.echo(f"City '{name}' already exists.")
        session.close()
        return
    city = City(name=name)
    session.add(city)
    session.commit()
    click.echo(f"Added city: {name}")
    session.close()

@click.command()
@click.argument('city_name')
@click.argument('temperature', type=float)
@click.argument('description')
def add_weather(city_name, temperature, description):
    """Add weather data for a city."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        if session.query(Weather).filter_by(city_id=city.id, date=date.today()).first():
            click.echo(f"Weather data for {city_name} on {date.today()} already exists.")
            session.close()
            return
        weather = Weather(city_id=city.id, date=date.today(), temperature=temperature, description=description)
        session.add(weather)
        session.commit()
        click.echo(f"Added weather for {city_name}: {temperature}C, {description}")
    else:
        click.echo("City not found")
    session.close()

@click.command()
@click.argument('city_name')
@click.argument('forecast')
def add_forecast(city_name, forecast):
    """Add a forecast for a city."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        forecast_entry = Forecast(city_id=city.id, date=date.today(), forecast=forecast)
        session.add(forecast_entry)
        session.commit()
        click.echo(f"Added forecast for {city_name}: {forecast}")
    else:
        click.echo("City not found")
    session.close()

@click.command()
@click.argument('city_name')
@click.option('--start-date', help='Start date in the format YYYY-MM-DD')
@click.option('--end-date', help='End date in the format YYYY-MM-DD')
def view_weather(city_name, start_date, end_date):
    """View weather data for a city."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        query = session.query(Weather).filter_by(city_id=city.id)
        if start_date:
            query = query.filter(Weather.date >= datetime.strptime(start_date, '%Y-%m-%d').date())
        if end_date:
            query = query.filter(Weather.date <= datetime.strptime(end_date, '%Y-%m-%d').date())
        weather_data = query.all()
        if weather_data:
            for weather in weather_data:
                click.echo(f"Date: {weather.date}, Temperature: {weather.temperature}C, Description: {weather.description}")
        else:
            click.echo("No weather data available for this city and date range.")
    else:
        click.echo("City not found")
    session.close()

@click.command()
@click.argument('city_name')
@click.option('--start-date', help='Start date in the format YYYY-MM-DD')
@click.option('--end-date', help='End date in the format YYYY-MM-DD')
def view_forecast(city_name, start_date, end_date):
    """View forecast data for a city."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        query = session.query(Forecast).filter_by(city_id=city.id)
        if start_date:
            query = query.filter(Forecast.date >= datetime.strptime(start_date, '%Y-%m-%d').date())
        if end_date:
            query = query.filter(Forecast.date <= datetime.strptime(end_date, '%Y-%m-%d').date())
        forecast_data = query.all()
        if forecast_data:
            for forecast in forecast_data:
                click.echo(f"Date: {forecast.date}, Forecast: {forecast.forecast}")
        else:
            click.echo("No forecast data available for this city and date range.")
    else:
        click.echo("City not found")
    session.close()

@click.command()
@click.argument('city_name')
@click.argument('new_name')
def update_city(city_name, new_name):
    """Update the name of a city."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        city.name = new_name
        session.commit()
        click.echo(f"Updated city name from {city_name} to {new_name}")
    else:
        click.echo("City not found")
    session.close()

@click.command()
@click.argument('city_name')
def delete_city(city_name):
    """Delete a city and all related data."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        session.delete(city)
        session.commit()
        click.echo(f"Deleted city {city_name} and all related data")
    else:
        click.echo("City not found")
    session.close()

@click.command()
@click.argument('city_name')
@click.argument('date_str')
def delete_weather(city_name, date_str):
    """Delete weather data for a city on a specific date."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        weather_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        weather = session.query(Weather).filter_by(city_id=city.id, date=weather_date).first()
        if weather:
            session.delete(weather)
            session.commit()
            click.echo(f"Deleted weather data for {city_name} on {date_str}")
        else:
            click.echo(f"No weather data found for {city_name} on {date_str}")
    else:
        click.echo("City not found")
    session.close()

@click.command()
@click.argument('city_name')
@click.argument('date_str')
def delete_forecast(city_name, date_str):
    """Delete forecast data for a city on a specific date."""
    session = Session()
    city = session.query(City).filter_by(name=city_name).first()
    if city:
        forecast_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        forecast = session.query(Forecast).filter_by(city_id=city.id, date=forecast_date).first()
        if forecast:
            session.delete(forecast)
            session.commit()
            click.echo(f"Deleted forecast data for {city_name} on {date_str}")
        else:
            click.echo(f"No forecast data found for {city_name} on {date_str}")
    else:
        click.echo("City not found")
    session.close()

cli.add_command(initdb)
cli.add_command(add_city)
cli.add_command(add_weather)
cli.add_command(add_forecast)
cli.add_command(view_weather)
cli.add_command(view_forecast)
cli.add_command(update_city)
cli.add_command(delete_city)
cli.add_command(delete_weather)
cli.add_command(delete_forecast)

if __name__ == '__main__':
    cli()
