# -*- coding: utf-8 -*-
from simplification_table import simplify_name_by_table
from simplification_table import simplify_name_by_store

def simplify_name(original_name):
    normalized_name=original_name.lower()
    (result, name_to_return) = simplify_name_by_table(normalized_name)
    if result == "not found" :
        print ("Not found position: ", normalized_name)
    return name_to_return

def get_store_category(name_of_store):
    (result, name_to_return) = simplify_name_by_store(name_of_store)
    if result == "not found" :
        print ("Not found racun issuer: ", name_of_store)
        return "Store"
    else :
        return name_to_return


def construct_importable_table(billing_table) :
    resulting = ""
    for record in billing_table :
        original_name=record["name"]
        name_of_store=record["name_of_store"]
        store_category = get_store_category(name_of_store)
        if store_category == "Store" :
             name=simplify_name(original_name)
        else :
            name = store_category
        quantity=record["quantity"]
        unit_price=record["unit_price"]
        total_per_product=record["total_per_product"]
        date=record["date"]
        comment=record["comment"]
        # Дата	Место	Источник	Позиция	Расход	Валюта расхода	Комментарий
        line= date + ";" + name_of_store + ";" + ";" + name + ";" + total_per_product + ";" + "RSD" + ";" + original_name + ". " + quantity + " units per " + unit_price + ". Comment: " + comment + "\n"
        resulting = resulting + line
    return resulting

