from turtle import clear
import boto3
import csv

ec2_cli=boto3.client(service_name ='ec2')

collect_all_regions =[]
for each_region in ec2_cli.describe_regions()['Regions']:
    collect_all_regions.append(each_region['RegionName'])
print(collect_all_regions)

fo=open('ec2_inven_new.csv','w',newline='')
data_obj=csv.writer(fo)
data_obj.writerow(["Sno","InstanceID","InstanceType","KeyName","Private_Ip","Public_Ip"])

cnt=1
for each_region in collect_all_regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
    for each_ins_in_reg in ec2_re.instances.all():

        data_obj.writerow([cnt,each_ins_in_reg.instance_id,each_ins_in_reg.instance_type,each_ins_in_reg.key_name,each_ins_in_reg.private_ip_address,each_ins_in_reg.public_ip_address])
        cnt+=1
def new_func(fo):
    fo.close()
new_func(fo)