import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# export PSQL_MYDB_URL='postgresql://bart:qwerty@localhost:5432/mydb'
engine = create_engine('postgresql://bart:qwerty@localhost:5432/mydb')
# engine = create_engine(os.getenv('PSQL_MYDB_URL'))
# to jesli sobie ustawie zmienna w linuchu
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    print(flights)
    print(flights[0])
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
