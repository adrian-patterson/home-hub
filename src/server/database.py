import os
import motor.motor_asyncio
from icc.models import PydanticObjectId


class SampleModel:
    id: str


class SampleDto:
    id: str


class Sample:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            "mongodb url")
        self.samples: motor.motor_asyncio.AsyncIOMotorCollection = self.db.sample_database.samples

    async def insert(self, sample: SampleDto) -> None:
        await self.samples.insert_one(sample.to_bson())

    async def find_all(self) -> list[SampleModel]:
        cursor: motor.motor_asyncio.AsyncIOMotorCursor = self.samples.find()
        return [SampleModel(**sample) for sample in await cursor.to_list(None)]

    async def find_by_name(self, name: str) -> SampleModel:
        return SampleModel(**(await self.samples.find_one({"name": name})))

    async def update(self, id: PydanticObjectId, sample: SampleDto) -> SampleModel:
        return SampleModel(**(await self.samples.find_one_and_replace({"_id": id}, sample.to_bson())))

    async def delete(self, id: PydanticObjectId) -> SampleModel:
        return SampleModel(**(await self.samples.find_one_and_delete({"_id": id})))
