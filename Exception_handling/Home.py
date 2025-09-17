import streamlit as st
from utiles.load_data import load_data
files = ["ticket_002_security_breach.json", 
             "ticket_003_network_outage.json",
                "ticket_004_email_spam.json",
                "ticket_005_software_license.json",
                "ticket_006_backup_corruption.json",
                "ticket_007_wireless_security.json",
                "ticket_008_database_performance.json",
                "ticket_009_phone_system_failure.json",
                "ticket_010_file_server_crash.json",
                "ticket_011_remote_desktop_issues.json",
                "ticket_012_antivirus_false_positive.json",
                "ticket_013_cloud_sync_issues.json",
                "ticket_014_printer_driver_conflict.json",
                "ticket_015_website_downtime.json",
                "ticket_016_mobile_device_management.json",
                "ticket_017_network_segmentation.json",
                "ticket_018_data_migration.json",
                "ticket_019_security_patch_deployment.json",
                "ticket_020_disaster_recovery_test.json"]

df = load_data(files)
# print(df.head())                 ### To see 1st 5 rows of the dataframe
# st.dataframe(df)                 ### To Visualize the dataframe using streamlit library
 
