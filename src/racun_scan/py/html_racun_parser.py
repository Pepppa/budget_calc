# -*- coding: utf-8 -*-
from lxml import html
import urllib.request
from simplification_table import simplify_name_by_table

store_data_panel_heading='Захтев за фискализацију рачуна'
resultig_data_panel_heading='Резултат фискализације рачуна'
bill_table_panel_heading='Спецификација рачуна'

name_of_store_label='Име продајног места'
total_amount_label='Укупан износ'
date_and_time_label='ПФР време (временска зона сервера)'
bill_table_aria_label='Invoice specification'



def get_store_data_element(tree) :
    for row in tree.xpath('//html/body/div[@class="container"]/div/form/div[@class="row"]') :
        for panel in row.findall('div/div[@class="panel panel-info"]') :
#            if panel.find('div[@class="panel-heading"]').text == store_data_panel_heading : # doesn't work, value isn't got correctly
             panelbody=panel.find('div[@class="panel-body"]')
             for formgroup in panelbody.findall('div[@class="form-group"]') :
                 if formgroup.find('label').text == name_of_store_label :
                     return panel.find('div[@class="panel-body"]')

def extract_store_data(tree, label) :
    data_for_store=get_store_data_element(tree)
    for element in data_for_store.findall('div[@class="form-group"]') :
        if element.find('label').text == label :
            return element.find('div/span').text


def get_resulting_data_element(tree) :
    for row in tree.xpath('//html/body/div[@class="container"]/div/form/div[@class="row"]') :
        for panel in row.findall('div/div[@class="panel panel-info"]') :
#            if panel.find('div[@class="panel-heading"]').text == resulting_data_panel_heading : # doesn't work, value isn't got correctly
             panelbody=panel.find('div[@class="panel-body"]')
             for formgroup in panelbody.findall('div[@class="form-group"]') :
                 if formgroup.find('label').text == total_amount_label :
                     return panel.find('div[@class="panel-body"]')

def extract_resulting_data(tree, label) :
    data_for_store=get_resulting_data_element(tree)
    for element in data_for_store.findall('div[@class="form-group"]') :
        if element.find('label').text == label :
            return element.find('div/span').text


def get_specific_table_class(tree, aria_label) :
    for row in tree.xpath('//html/body/div[@class="container"]/div/form/div[@class="row"]') :
        for panel in row.findall('div/div[@class="panel panel-info"]') :
            if panel.find('div[@class="panel-body"]') is not None :
                panelbody=panel.find('div[@class="panel-body"]')
            else :
                panelbody=panel.find('div[@id="collapse-specs"]/div[@class="panel-body"]')
            table_class=panelbody.find('div/table[@aria-label="' + aria_label + '"]')
            if table_class is not None :
                return table_class


def extract_invoice_table(tree, aria_label) :
    table_class=get_specific_table_class(tree, aria_label)
    list_of_products = []
    for tablerow in table_class.findall('tbody/tr') :
        if tablerow.find('td[@data-bind="text: Name"]') is not None :
            name=tablerow.find('td[@data-bind="text: Name"]').text
        else :
            name=tablerow.find('td/strong[@data-bind="text: Name"]').text

        quantity=tablerow.find('td[@data-bind="decimalAsText: Quantity"]').text
        unit_price=tablerow.find('td[@data-bind="decimalAsText: UnitPrice"]').text
        total_per_product=tablerow.find('td[@data-bind="decimalAsText: Total"]').text.replace(".","")
        pos={"name" : name, "quantity": quantity, "unit_price": unit_price, "total_per_product": total_per_product }
        list_of_products.append(pos)
    return list_of_products


def get_name_of_store(tree) :
    return extract_store_data(tree, name_of_store_label)

def get_total_amount(tree) :
    amount_raw=extract_resulting_data(tree, total_amount_label)
    return amount_raw.strip()

def get_date(tree) :
    date_and_time_raw=extract_resulting_data(tree, date_and_time_label)
    date_and_time=date_and_time_raw.strip()
    (date, time)=date_and_time.split()
    return date

def get_table(tree) :
    return extract_invoice_table(tree, bill_table_aria_label)

def simplify_name(original_name):
    normalized_name=original_name.lower()
    (result, name_to_return) = simplify_name_by_table(normalized_name)
    if result == "not found" :
        print ("Not found position: ", normalized_name)
    return name_to_return


def construct_importable_table(billing_table, name_of_store, date) :
    resulting = ""
    for record in billing_table :
        original_name=record["name"]
        name=simplify_name(original_name)
        quantity=record["quantity"]
        unit_price=record["unit_price"]
        total_per_product=record["total_per_product"]
        # Дата	Место	Источник	Позиция	Расход	Валюта расхода	Комментарий
        line= date + ";" + name_of_store + ";" + ";" + name + ";" + total_per_product + ";" + "RSD" + ";" + original_name + ". " + quantity + " units per " + unit_price + ". \n"
        resulting = resulting + line
    return resulting

def retrieve_html_from_file(filename) :
    with open(filename, 'r') as file:
        data = file.read()
    return data

def retrieve_html_from_url(url) :
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def extract_all_positions_as_table(data) :

    tree = html.fromstring(data)

    name_of_store=get_name_of_store(tree)
    print("Name of store", name_of_store)

    total_amount=get_total_amount(tree)
    print("Total amount", total_amount)

    date=get_date(tree)
    print("Date", date)

    billing_table=get_table(tree)
    for_print = construct_importable_table(billing_table, name_of_store, date)

    return for_print

