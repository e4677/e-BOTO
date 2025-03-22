from models.officer import Officer
from services.main_service import MainService


class OfficerService(MainService):
    OFFICER_FILE = "officer.json"

    @classmethod
    def load_officers(cls):
        """Load officer data from JSON file."""
        return cls.load_data(cls.OFFICER_FILE)

    @staticmethod
    def login(officer_id, pin):
        officers = OfficerService.load_officers()

        for officer in officers:
            if officer["officerID"] == officer_id and officer["PIN"] == pin:
                return {"officerID": officer["officerID"], "name": officer["name"]}
        return None
