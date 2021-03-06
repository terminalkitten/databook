# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from airflow.hooks.dbapi_hook import DbApiHook
from sqlalchemy import create_engine


class AlchemyHook(DbApiHook):
    """
    Interact with any database
    """

    conn_name_attr = 'db_conn_id'
    default_conn_name = 'db_default'

    def __init__(self, *args, **kwargs):
        super(AlchemyHook, self).__init__(*args, **kwargs)

    def get_conn(self):
        """
        Returns an alchemy connection object
        """
        conn = self.get_connection(self.db_conn_id)
        engine_url = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
            conn.conn_type,
            conn.login,
            conn.password,
            conn.host,
            conn.port,
            conn.schema
            )

        engine = create_engine(engine_url)
        return engine

    def get_db(self):
        conn = self.get_connection(self.db_conn_id)
        return conn.schema
