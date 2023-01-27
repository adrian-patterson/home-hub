from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from server.database import Sample
from icc.models import PydanticObjectId


class SampleDto:
    id: str


router = APIRouter()
scene_repository = Sample()


@router.post("", summary="Create a sample", response_description="The created sample")
async def create_sample(sample: SampleDto):
    await scene_repository.insert(sample)
    return sample.to_json()


@router.get("", summary="Get all scenes", response_description="List of all scenes")
async def get_all_samples():
    scenes = await scene_repository.find_all()
    return jsonable_encoder(scenes)


@router.put("/{id}", summary="Update a sample", response_description="Updated sample object")
async def update_sample(id: PydanticObjectId, sample: SampleDto):
    updated_sample = await scene_repository.update(id, sample)
    return jsonable_encoder(updated_sample)


@router.delete("/{id}", summary="Delete a sample", response_description="Deleted sample")
async def delete_sample(id: PydanticObjectId):
    deleted_sample = await scene_repository.delete(id)
    return jsonable_encoder(deleted_sample)
