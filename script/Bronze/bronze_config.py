extract_config = [


    {
        'table_name': 'bronze.crm_cust_info',
        'path': '/Volumes/workspace/bronze/source_systems/source_crm/cust_info.csv',
        'mode': 'overwrite',
        'source' : 'crm'


    },
    {
        'table_name': 'bronze.crm_prd_info',
        'path': '/Volumes/workspace/bronze/source_systems/source_crm/prd_info.csv',
        'mode': 'overwrite',
        'source' : 'crm'

    },

    {
        'table_name': 'bronze.crm_sales_details',
        'path': '/Volumes/workspace/bronze/source_systems/source_crm/sales_details.csv',
        'mode': 'overwrite',
        'source' : 'crm'

    },

    {
        'table_name': 'bronze.erp_cust_az12',
        'path': '/Volumes/workspace/bronze/source_systems/source_erp/CUST_AZ12.csv',
        'mode': 'overwrite',
        'source' : 'erp'

    },
    {
        'table_name': 'bronze.erp_loc_a101',
        'path': '/Volumes/workspace/bronze/source_systems/source_erp/LOC_A101.csv',
        'mode': 'overwrite',
        'source' : 'erp'

    },
    {
        'table_name': 'bronze.erp_px_cat_g1v2',
        'path': '/Volumes/workspace/bronze/source_systems/source_erp/PX_CAT_G1V2.csv',
        'mode': 'overwrite',
        'source' : 'erp'

    },

]


