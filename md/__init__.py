# Copyright (c) Sunlight Foundation, 2014, under the terms of the BSD-3
# license, a copy of which is in the root level LICENSE file.
#   Benjamin Atwood <batwood@PC101561.local>

from pupa.scrape import Jurisdiction, Post, Organization
from .people import MarylandPersonScraper


class Maryland(Jurisdiction):
    division_id = 'ocd-division/country:us/state:ak'
    classification = 'government'
    name = "Maryland State Government"
    url = 'http://maryland.gov/'

    scrapers = {
        "people": MarylandPACScraper,
    }

    def get_organizations(self):
        org = Organization(name='Maryland Executive Branch',
                           classification='executive')
        yield org
