from uuid import uuid4

import pytest

from src.models.settings.connection import db_connection_handler

from .events_repository import EventsRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="new register on db")
def test_insert_events():
    event = {
        "uuid": str(uuid4()),
        "title": "Meu Title",
        "slug": "Meu Slug Aqui",
        "maximum_attendees": 20,
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)

    print(response)


@pytest.mark.skip(reason="useless")
def test_get_event_by_id():
    event_id = "c054b2ef-1409-4c69-99cc-441019e515a8"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)

    print(response)
