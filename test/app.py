
from flask import (
    make_response,     
    abort,
)
 from config import db
 from models import (
     Person,
     PersonSchema,
)

def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    people = Person.query \
        .order_by(Person.lname) \
        .all()

    # Serialize the data for the response
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people).data
