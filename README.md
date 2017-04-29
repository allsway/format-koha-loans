# format-koha-loans
Turns Koha loans into format that can be uploaded through Alma Offline circ

#### parse_koha_users.py
Parses a csv export of Koha loans and:
- transalates user name into user ID that will be used in Alma
- outputs file in correct offlinecirc.dat format:
`201704281804L3000000059935                                                                       aSway`

Run as 
`python parse_koha_users.py users.csv > offlinecirc.dat`

#### Alma steps
Navigate to Offline Circulation and upload your offlinecirc.dat file.  All users and barcodes in the offlinecirc.dat file must exist in Alma for the loans to process. 
