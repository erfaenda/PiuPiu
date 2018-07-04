#! /usr/bin/env python
# -*- coding: utf-8 -*-

import configparser, random, time


def write_data_DHT22(path):
    while True:
        t = random.randint(1,27)
        h = random.randint(10, 99)

        """
        Create a config file
        """
        config = configparser.ConfigParser()
        config.add_section("DHT22_last")
        config.set("DHT22_last", "temperature", "{}".format(t))
        config.set("DHT22_last", "humi", "{}".format(h))


        with open(path, "w") as config_file:
            config.write(config_file)
        time.sleep(2)

if __name__ == "__main__":
    path = "DHT22.ini"
    write_data_DHT22(path)