from Connect import Connection
import json

class dataimport:


    def main():
        # read json and store it in table
        connection = Connection()
        cursor = connection.cursor
        f = open('./db.json')
        jsonToDict = json.load(f)
        loadedData = jsonToDict["News"]
        print(loadedData)
        # # first create table
        #
        # # Create table of Organization
        # # ORGANIZATION_CREATE = "CREATE TABLE `app_db`.`organization` (`Id` INT NOT NULL AUTO_INCREMENT , `Name` VARCHAR(50) NOT NULL , `Address` VARCHAR(50) NOT NULL , `Phone` VARCHAR(50) NOT NULL , `Email` VARCHAR(20) NOT NULL , `OrganizationType` VARCHAR(20) NOT NULL , `OrganizationCreated` TIMESTAMP NOT NULL , PRIMARY KEY (`Id`))"
        # # cursor.execute(ORGANIZATION_CREATE)
        # # REALTOR_TABLE = "CREATE TABLE `app_db`.`Realtor` (`Id` INT NOT NULL AUTO_INCREMENT , `Name` VARCHAR(50) NOT NULL , `Phone` VARCHAR(10) NOT NULL , `Email` VARCHAR(20) NOT NULL , `FirstName` VARCHAR(50) NOT NULL , `LastName` VARCHAR(50) NOT NULL , `OrganizationId` INT , FOREIGN KEY (OrganizationId) REFERENCES organization(id) , PRIMARY KEY (`Id`))"
        # # cursor.execute(REALTOR_TABLE)
        # # PROPERTY_TABLE = "CREATE TABLE `app_db`.`Property` (`Id` INT NOT NULL AUTO_INCREMENT , `Description` VARCHAR(50) NOT NULL , `PropertyType` VARCHAR(10) NOT NULL , `LandSize` VARCHAR(20) NOT NULL , `PostalCode` VARCHAR(50) NOT NULL , `ListingDate` TIMESTAMP NOT NULL  , `RealtorId` INT , FOREIGN KEY (RealtorId) REFERENCES realtor(id) , PRIMARY KEY (`Id`))"
        # # cursor.execute(PROPERTY_TABLE)
        #
        # for data in loadedData:
        #     sourcedata = data['Realtor']
        #     realtorData = data['Realtor']
        #     realtorData = data['Realtor']
        #     # print(organizationData)
        #
        #     # INSERT_ORGANIZATION = "insert into organization (Name, Address, Phone, Email, OrganizationType, OrganizationCreated) values ('%s', '%s','%s','%s','%s','%s')" %(organizationData['Name'], organizationData['Address'], organizationData['Phone'], organizationData['Email'], organizationData['OrganizationType'], organizationData['OrganizationCreated'])
        #     # cursor.execute(INSERT_ORGANIZATION)
        #     # check weather organization exists or not
        #     CHECK_EXISITING_ORGANIZATION = """select id from organization where Name = %s"""
        #
        #     print(CHECK_EXISITING_ORGANIZATION, (organizationData['Name'],))
        #
        #     cursor.execute(CHECK_EXISITING_ORGANIZATION, (organizationData['Name'],))
        #
        #     exisiting_organization_id = cursor.fetchone()
        #
        #     print(exisiting_organization_id)
        #
        #     if (len(exisiting_organization_id) != 0):
        #         # print("Already organization exist")
        #         INSERT_REALTOR = "insert into realtor (Name, OrganizationId, Phone, Email, FirstName, LastName) values ('%s', '%d','%s','%s','%s','%s')" % (
        #         realtorData['Name'], exisiting_organization_id, realtorData['Phone'], realtorData['Email'],
        #         realtorData['FirstName'], realtorData['LastName'])
        #
        #     else:
        #         INSERT_ORGANIZATION = "insert into organization (Name, Address, Phone, Email, OrganizationType, OrganizationCreated) values ('%s', '%s','%s','%s','%s','%s')" % (
        #         organizationData['Name'], organizationData['Address'], organizationData['Phone'], organizationData['Email'],
        #         organizationData['OrganizationType'], organizationData['OrganizationCreated'])
        #         cursor.execute(INSERT_ORGANIZATION)
        #
        # connection.CloseConnection()


    if __name__ == "__main__":
        main()