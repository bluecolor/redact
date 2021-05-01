# from app.vendors.mssql.mssql import SqlServer


vendors = {}


def register_vendor(vendor_class):
    vendors[vendor_class.type()] = vendor_class
