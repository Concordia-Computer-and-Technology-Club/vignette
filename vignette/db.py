"""
db.py
Ian Kollipara
2022.10.03

Database Interactions
"""

# Imports
from tortoise import Tortoise, fields
from tortoise.models import Model


class Aircraft(Model):
    """Aircraft Table.

    This table holds the data for all the planes and such.
    It connects to personnel through AircraftPersonnel.
    """

    id = fields.UUIDField(pk=True)
    aircraft_number = fields.TextField()
    squad_code = fields.TextField()
    aircraft_type = fields.CharField(max_length=5)
    name = fields.TextField()
    missing_air_crew_report_number = fields.IntField()
    misc = fields.JSONField()


class Personnel(Model):
    """Personnel Table.

    This contains all pilots and other people who are associated
    with the planes.
    """

    id = fields.UUIDField(pk=True)
    first_name = fields.TextField()
    last_name = fields.TextField()
    nickname = fields.TextField()
    rank = fields.TextField()
    job = fields.TextField()
    unit = fields.TextField()
    misc = fields.JSONField()


class OutsideReferences(Model):
    """OutsideReferences Table.

    This is a collection of references for each personnel member.
    A personnel member can have 0 or more outside references.
    """

    id = fields.UUIDField(pk=True)
    personnel_id = fields.ForeignKeyField("models.Personnel")
    reference = fields.TextField()


class AircraftPersonnel(Model):
    """AircraftPersonnel Table.

    This is the table that connects Aircraft and their
    corresponding personnel.
    """

    id = fields.UUIDField(pk=True)
    aircraft = fields.ForeignKeyField("models.Aircraft")
    personnel = fields.ForeignKeyField("models.Personnel")
    role = fields.TextField()
