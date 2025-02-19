from mirror.celery import app
from library.db_connection_factory import get_collection
from app.learning.models import TransientModel, ModelContainer
from library.collection_utils import list_to_dict
# import tensorflow as tf
import pandas as pd
# from celery.decorators import shared_task

# logger=get_task_logger(__name__)

# This is the decorator which a celery worker uses
# @shared_task(name="test_task")
@app.task(bind=True)
def train_model(self, tenant):
    model = TransientModel(tenant)
    # model.initialize_vectorizer(pd.DataFrame(list(get_collection(tenant, 'dataset_train').find({}))))
    print('initializing vectorizer')
    model.initialize_vectorizer()
    print('initialized vectorizer')
    label_map = {}
    index = 0
    for label_item in get_collection(tenant, 'dataset_train').find({}).distinct('label'):
        label_map[label_item] = index
        index = index + 1

    #model.train(tenant, label_map, pd.DataFrame(list(get_collection(tenant, 'dataset_train').find({}))), pd.DataFrame(list(get_collection(tenant, 'dataset_test').find({}))))
    model.train(tenant)
    return {'label_count': 'label_count'}
