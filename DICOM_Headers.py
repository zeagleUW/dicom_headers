import os
import csv
import pydicom

#Folder to read dicom files from
dicom_file_location = "./dicom"

#Name of output file
output_file = './dicom_data2.csv'

#List of headers you want to extract to CSV
headers = {"PatientName","PatientID", "KVP"}

def create_CSVHeaders(headers, csvwriter):
	dicom = []
	for header in headers:
		dicom.append(header)
	csvwriter.writerow(dicom)

def main():
	dicom_data = open(output_file, 'w', newline='')
	csvwriter = csv.writer(dicom_data)
	create_CSVHeaders(headers, csvwriter)

	for dicomfile in os.listdir(dicom_file_location):
		ds = pydicom.dcmread(dicom_file_location+"/"+dicomfile)
		dicom = []
		for header in headers:
			dicom.append(ds.get(header))
		csvwriter.writerow(dicom)

	dicom_data.close()

if __name__ == "__main__":
    main()
