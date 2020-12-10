import sqlite3
from model import DataKnowledge
import datetime
import json


connection = sqlite3.connect('knowledge.db', check_same_thread=False)
cursor = connection.cursor()


def getAllComponents():
    commandSelect = """SELECT 
                        component_id,
                        component_type, 
                        component_name, 
                        property_name, 
                        property_value, 
                        datelastevent  
                    FROM 
                        controller_components"""

    cursor.execute(commandSelect)
    results = [dict((cursor.description[i][0], value)
                    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return results


def updateDataKnowledge(param: DataKnowledge):
    performUpdate(1, param.cpuFailureRate)
    performUpdate(2, param.scalabilityaDesiredReplicas)
    performUpdate(3, param.fidelityaDesiredReplicas)
    performUpdate(4, param.scalabilitybDesiredReplicas)
    performUpdate(5, param.fidelitybDesiredReplicas)


def performUpdate(component_id, property_value):
    updateCommand = """
                    UPDATE 
                        controller_components 
                    SET 
                        property_value = ?,
                        datelastevent = ?
                        
                    WHERE
                        component_id = ?

                    """
    data_tuple = (property_value,
                  datetime.datetime.now(), component_id,)
    cursor.execute(updateCommand, data_tuple)
    connection.commit()


def loadInitialKnowledge():

    tabComponents = """CREATE TABLE IF NOT EXISTS 
                        controller_components(  component_id INTEGER PRIMARY KEY, 
                                                component_type VARCHAR(50),
                                                component_name VARCHAR(50), 
                                                property_name VARCHAR(50),
                                                property_value TEXT,
                                                datelastevent timestamp
                                            )"""

    cursor.execute(tabComponents)

    date_tuple = (str(datetime.datetime.now()),)

    insertComponent1 = """INSERT INTO controller_components (
                                                component_id,
                                                component_type,
                                                component_name,
                                                property_name,
                                                property_value,
                                                datelastevent
                                    ) VALUES (
                                                1,
                                                'Deployment',
                                                'FailureManager',
                                                'cpuFailureRate',
                                                '0.0',
                                                ?
                                                            ) """

    cursor.execute(insertComponent1, date_tuple)

    insertComponent2 = """INSERT INTO controller_components (
                                                component_id,
                                                component_type,
                                                component_name,
                                                property_name,
                                                property_value,
                                                datelastevent
                                    ) VALUES (
                                                2,
                                                'Deployment',
                                                'Scalabilitya',
                                                'desiredReplicas',
                                                '0',
                                                ?
                                                            ) """

    cursor.execute(insertComponent2, date_tuple)

    insertComponent3 = """INSERT INTO controller_components (
                                                component_id,
                                                component_type,
                                                component_name,
                                                property_name,
                                                property_value,
                                                datelastevent
                                    ) VALUES (
                                                3,
                                                'Deployment',
                                                'Fidelitya',
                                                'desiredReplicas',
                                                '0',
                                                ?
                                                            ) """

    cursor.execute(insertComponent3, date_tuple)

    insertComponent4 = """INSERT INTO controller_components (
                                                component_id,
                                                component_type,
                                                component_name,
                                                property_name,
                                                property_value,
                                                datelastevent
                                    ) VALUES (
                                                4,
                                                'Deployment',
                                                'Scalabilityb',
                                                'desiredReplicas',
                                                '0',
                                                ?
                                                            ) """

    cursor.execute(insertComponent4, date_tuple)

    insertComponent5 = """INSERT INTO controller_components (
                                                component_id,
                                                component_type,
                                                component_name,
                                                property_name,
                                                property_value,
                                                datelastevent
                                    ) VALUES (
                                                5,
                                                'Deployment',
                                                'Fidelityb',
                                                'desiredReplicas',
                                                '0',
                                                ?
                                                            ) """
    cursor.execute(insertComponent5, date_tuple)

    connection.commit()
