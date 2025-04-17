# -*- coding: utf-8 -*-
import csv

def convert_price_to_printable_srt(price_f) :
    return str(round(price_f,2)).replace(".",",")

def extract_all_positions_as_dict (csvfilepath) :
    list_of_products = []
    sum_by_now = 0
    current_racun_id = ""

    with open(csvfilepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if len(row) != 8 :
                print("Can't handle row " + ";".join(row))
                continue
            # Tip; Datum i vreme; Naziv kompanije; Ime prodajnog mesta; Svrha plaćanja; Naziv artikla; Količina; Ukupna cena
            [type_of_racun, date_and_time, short_name_of_store, code_of_store, type_of_payment, name, quantity, total_per_product] = row
            total_per_product_f = float(total_per_product)
            quantity_f = float(quantity)


            if type_of_racun == 'Tip' :
                continue
            if short_name_of_store == "" :
                full_name_of_store = code_of_store
            else :
                full_name_of_store = short_name_of_store + " - " + code_of_store
            [date, time] = date_and_time.split(" ")

            unit_price_f = total_per_product_f / quantity_f

            pr_quantity = convert_price_to_printable_srt(quantity_f)
            pr_unit_price = convert_price_to_printable_srt(unit_price_f)
            pr_total_per_product = convert_price_to_printable_srt(total_per_product_f)
            pos={"name" : name, "quantity": pr_quantity, "unit_price": pr_unit_price, "total_per_product": pr_total_per_product, "date": date, "name_of_store": full_name_of_store, "date_and_time": date_and_time }
            list_of_products.append(pos)

            # calculate total amount of the whole racun
            if current_racun_id == date_and_time :
                sum_by_now += total_per_product_f
            else :
                sum_by_now = total_per_product_f
                current_racun_id = date_and_time

            pr_sum_by_now = convert_price_to_printable_srt(sum_by_now)
            for position in list_of_products :
                if position["date_and_time"] == date_and_time :
                    position["comment"] = "Total amount in racun: " + pr_sum_by_now
    return list_of_products
