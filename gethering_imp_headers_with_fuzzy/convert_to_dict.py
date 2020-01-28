import json

if __name__=="__main__":
    outer_elements=[['name', 'name1', 'f_name', 'cname', 'i_name', 'name2', 'fname', 'mname', 'lname'], ['email', 'email id', 'email1', 'emailid', 'e-mail', 'e_mail', 'emailid1', 'emailid2', 'email2', 'emails', 'email_id'], ['contact', 'contact_ph1', 'contactp'], ['address', 'address1', 'address2', 'address3', 'adders', 'address4', 'adderss', 'addresss','postal address'], ['area'], ['landmark', 'landmarks', 'land mark'], ['pincode', 'pin code', 'pin_code', 'pincode_no'], ['city', 'city_', 'city_1'], ['website', 'web_site', 'web site'], ['url'], ['mdn_status', 'status'], ['circle_id', 'circle'], ['del_number', 'number'], ['customer_name', 'customer_segment'], ['del_activation_date'], ['service_start', 'service_pr'], ['typeofconn'], ['acctcatgy'], ['sub_acct_category', 'sub_categoty'], ['revrcvcostctr'], ['owngcostctr'], ['equip_status'], ['bill_period'], ['credit_rating'], ['bill_fname', 'bill_lname', 'bill_name_pre'], ['bill_company', 'company'], ['bill_address1', 'bill_address2', 'bill_address3'], ['telephone_no', 'telephone', 'telephone1', 'telephone2', 'telephone3', 'telephone no_', 'telephone no_1', 'telephone no_2', 'telephone 1', 'telephone 2', 'telephone 3','tel no_', 'telno', 'tel nos', 'tel  no 1', 'tel no 2', 'tel no'], ['sanjeev'], ['first name', 'last name', 'sir name', 'cust name'], ['company name', 'companyname', 'compname', 'company_name', 'company name_1', 'company names', 'companies name', 'comopany name'], ['alternate number', 'contract number'], ['bill_fname bill_lname'], ['name of the candidate', 'name of the co'], ['e-mail address', 'email address','emailaddress', 'e_mail_address'], ['telephone numbers', 'phonenumber', 'phone number', 'phone number_1', 'phone_number'], ['date of birth', 'date_of_birth'], ['work experience', 'experience'], ['resume title', 'resume id'], ['key skills'], ['functional area', 'current functional area'], ['current location', 'preferred location'], ['current employer', 'current role'], ['current designation', 'designation', 'designation1', 'designation2', 'ceo designation'], ['annual salary'], ['u_g_ course', 'course'], ['com', 'conm'], ['mob', 'mobno'], ['loc'], ['current salary', 'current industry'], ['course(highest education)', 'specialization(highest education)', 'institute(highest education)'], ['gender'], ['age', 'large'], ['description', 'sic_description'], ['addr1', 'addr2', 'addr3', 'add', 'addre'], ['person', 'kpers'], ['profile', 'role'], ['store name', 'customer name'], ['locality', 'sub_locality'], ['building_name'], ['stdcode', 'postalcode'], ['ptc_name', 'cust_name', 'co_name', 'cus_name', 'sort_name', 'ceo_name'], ['companyemail', 'company_na'], ['level1', 'level2', 'level3', 'level'], ['name of college'], ['add 1', 'add 2', 'add 3'], ['fax_no','fax no_', 'faxno', 'fax nos', 'fax no', 'fxno'], ['e- mail', '[email]', 'email_2', 'mail', 'coemail', 'e_mail1', 'email-2', 'email-1'], ['owners name', 'zonename', 'ownername'], ['location', 'education'], ['area of specialization', 'specialisation', 'specialization'], ['industry'], ['previous employer'], ['course(2nd highest education)', 'specialization(2nd highest education)', 'institute(2nd highest education)'], ['last'], ['active', 'activities'], ['date', 'date_1', 'date_2'], ['add1', 'add2', 'add3', 'add4', 'add5'], ['state', 'stat'], ['pin', 'pino'], ['phone_res', 'phone', 'phone_no', 'phone_1', 'phone_2'], ['creadit limit', 'credit_limit'], ['date activate', 'active deactive'], ['category', 'category(1)', 'category_id', 'categroy'], ['serial no', 'sl no', 'sr no'], ['contactname', 'contact no', 'contact name 1', 'contact name2'], ['searchstring'], ['mob-number', 'ph-number'], ['place'], ['sl_no', 'sr_no', 'res_no', 's_no'], ['contact person', 'contact_person', 'office contact person', 'contactperson', 'contact person1', 'contact person2', 'contact persone', 'contact person_1'], ['phone 1', 'phone1', 'phone2', 'phone3', 'phone4', 'phone5', 'phone6', 'phoneno', 'ophone', 'phone no', 'phone 2', 'phone 3'], ['comments', 'comments1'], ['id'], ['loan_type', 'rln_type'], ['exe_name', 'per_name'], ['remarks', 'remark', 'remarks_1', 'remarks_2'], ['ext', 'extn'], ['residence', 'residence phone', 'residence #'], ['[source]', 'source'], ['srno', 'sr_no_'], ['fax'], ['products dealing into', 'products dealing'], ['branch', 'exambranch'], ['keywords'], ['prefix'], ['caller', 'called'], ['clasname', 'car name', 'cardname', 'catname'], ['elangovan'], ['consign_name', 'colongname'], ['middle name', 'middle_nam'], ['surname'], ['res no', 's no'], ['off no', 'off_no'], ['month'], ['year'], ['ci-code', 'isdcode', 'code', 'zipcode'], ['res', 'res_1'], ['offphone', 'off ph', 'off phone'], ['having cc', 'having car'], ['income level'], ['class'], ['off_name', 'off_name_1', 'fm_name', 'fm_name_e'], ['job title', 'title', 'ceo title'], ['department'], ['address 1', 'address 2', 'address 3', 'address 4', 'address_1', 'address_2', 'address 5', 'address -2', 'address -3', 'address_3', 'address-1', 'address-2'], ['email address (work)'], ['d o b', 'dob'], ['pan/f60'], ['of', 'off'], ['lan_1', 'lan_2'], ['per_email', 'partyemail'], ['res_city', 't_city', 'cust_city'], ['off_city'], ['res_add1', 'res_add2'], ['res_pin', 'resi'], ['off_add1', 'off_add2'], ['off_pin'], ['pre'], ['car'], ['add_1', 'add_2', 'add_3'], ['agent name', 'student name'], ['team leaders'], ['appoint address', 'site address'], ['doc'], ['time', 'time_1'], ['field executive'], ['field status'], ['office address', 'regd_office address'], ['d/o/b'], ['fetl'], ['vrouter', 'vrouter_1'], ['exp_ (yrs)'], ['employers', 'employees', 'employer'], ['roles'], ['current annual salary (rs_ in lacs)'], ['doj'], ['dept', 'deposit'], ['chennai city pincodes'], ['cp1', 'c1'], ['desig1', 'desig2', 'desig', 'designa_', 'design1', 'design2'], ['cp2', 'c2'], ['activity1', 'activity2'], ['database of talent-kerala'], ['project name', 'project type'], ['project status'], ['project cost (rs_ crore)'], ['project ownership'], ['raw materials', 'rawmaterial'], ['contract basis', 'contract status'], ['regd_office tel no', 'regd_office fax no'], ['site tel no', 'site fax no'], ['project key person1', 'project key person1 designation', 'project key person2', 'project key person2 designation'], ['email_addr', 'e mail add'], ['contact no - residence'], ['qualification', 'academic qualification'], ['salary'], ['cityname', 'city name', 'custname'], ['c3'], ['excel sheet download'], ['serial number'], ['bank_name', 'bank_agency_name'], ['ctc'], ['spe'], ['u_g'], ['institute'], ['country', 'account'], ['icqno', 'iecno'], ['pagerno', 'part_no'], ['categories'], ['tollfreenumber'], ['other phone'], ['turnover'], ['capital'], ['other location', 'other_location', 'customer location'], ['product category', 'product type'], ['city code', 'ctc code', 'std code', 'cust code'], ['ctc no', 'ctc no_1'], ['mail id', 'e-mail id'], ['web'], ['product', 'producer', 'products'], ['member code', 'member name', 'member'], ['sebi registration no_', 'sebi reg_ no_'], ['nature of office'], ['ceo name', 'person name'], ['district'], ['constitution'], ['maincategory'], ['phone nos_'], ['fax std code', 'faxstdcode'], ['postal code', 'zip/postal code'], ['currently working in'], ['occupation'], ['two wheeler', 'four wheeler'], ['established', 'year established'], ['college name', 'college'], ['state / city'], ['address line 1', 'address line 2', 'address line 3'], ['tel_2', 'tel', 'tel_1', 'tel_o', 'tel_r'], ['reg_ address', 'corr_ address'], ['md'], ['exnm'], ['ardesc', 'cadesc'], ['ctdesc', 'scdesc', 'con_desc'], ['dsdesc'], ['prdesc', 'per_desg'], ['poad'], ['pnno'], ['profile_1'], ['addaddress1', 'addaddress2', 'addaddress3'], ['addcity'], ['addpin'], ['addemail'], ['addalternate', 'candidatename'], ['addweb'], ['fax number', 'fax_number'], ['contact person degination'], ['corporate/marketing/media contact person & degination'], ['degnation'], ['std'], ['annual turnover'], ['bankers'], ['importing countries'], ['international import'], ['importing_from', 'imports_from'], ['intr_imp'], ['businessdetails', 'business details'], ['chiefexec'], ['region', 'aggregation'], ['telex', 'tele_1', 'tele_2'], ['catprod', 'trdprod', 'dtlprod'], ['mfdprod'], ['field15', 'field16', 'field17', 'field18', 'field19', 'field20', 'field21', 'field22', 'field23', 'field24', 'field25', 'field26', 'field27', 'field5', 'field6', 'field13', 'field14'], ['exhibitor_name'], ['contact_person_name'], ['dist'], ['phon1', 'phon2', 'phon3', 'phon4'], ['des1', 'des2', 'desg'], ['p_name1', 'p_name2'], ['fullproduct'], ['auth_per1', 'auth_per2'], ['desg_per1', 'desg_per2'], ['prod_codes'], ['acct_nm', 'ac_nm_v'], ['street'], ['site', 'size'], ['exe_desg', 'ceo_desig'], ['car owner name'], ['first_name', 'last_name'], ['h_no', 'htno'], ['sex'], ['type'], ['addition_d'], ['form_no', 'fvtm_no'], ['promotion_'], ['merchant_i'], ['birth_plac'], ['make'], ['diesel'], ['petrol'], ['mode_of_pa'], ['applied_da'], ['business profile', 'businesstype'], ['telstdcode'], ['eef'], ['visa issued', 'tickets issued'], ['visa tomorrow'], ['tel office', 'office'], ['tel 1'], ['direct tel'], ['account manager'], ['assn_'], ['sr'], ['name of company'], ['concern_ person'], ['follow up'], ['meeting date & time'], ['attended'], ['pindoce'], ['partywebsite'], ['diractivities'], ['acronym'], ['prodsrv'], ['ceo_first_name', 'ceo_last_name'], ['sprkey'], ['tel_no1', 'tel_no2', 'tehsil_no'], ['person1', 'person2', 'person3'], ['rooms'], ['desg1', 'desg2'], ['cuisine'], ['company_namedisplay'], ['physical_address1', 'physical_address2'], ['physical_major_town'], ['physical_postcode'], ['web_address'], ['turnoverdisplay'], ['capitaldisplay'], ['office_hours'], ['quality_assessment'], ['members_of'], ['exports_to'], ['yoe'], ['products/services', 'product base price'], ['father name', 'dealer name'], ['sno', 'slno'], ['admno'], ['total'], ['rank'], ['result'], ['kolkata it directory'], ['re: companies address with hr email ids'], ['indian website adress'], ['all india computer related data'], ['email address at aiims'], ['garments fashion readymade'], ['hotel name', 'co name'], ['citywise'], ['hotel_web'], ['chain_web'], ['sales_mktg'], ['ownership'], ['ceo_md'], ['g_manager'], ['pharmaceuticals and bio tech companies in india'], ['list of companies with hr details'], ['adphone1'], ['kolkata'], ['vehicle', 'vechile'], ['loan', 'land'], ['tenor', 'tenure'], ['ath3_name_line_1'], ['ath3_addr_1', 'ath3_addr_2', 'ath3_addr_3', 'ath3_addr_4'], ['ath3_city'], ['ath3_zip_code'], ['bio-technology in bangalore'], ['state/province', 'state/prov'], ['tool free phone'], ['service or product description'], ['group classification'], ['rating'], ['opening hours'], ['search keyword'], ['search location'], ['latitude', 'longitude'], ['map link'], ['record id'], ['date add'], ['second_name', 'vendor_name'], ['bill_city', 'bill_zip'], ['bill_state'], ['income', 'oth_income'], ['female'], ['card_no', 'idcard_no'], ['card_creat'], ['app_firstn'], ['app_middle'], ['app_lastna'], ['app_dob', 'app_ no'], ['app_temp_c'], ['perm_addre', 'perm_addr1', 'perm_addr2'], ['perm_citys', 'user_city'], ['perm_pinco'], ['perm_telno'], ['off_telno'], ['gross_ann_'], ['certification'], ['currentemployer'], ['catelog_url'], ['firstname', 'lastname'], ['gridcolumn2'], ['cat_id'], ['loan amt'], ['landline', 'land line', 'landline-1', 'landline-2'], ['business name'], ['street address'], ['operator'], ['tag'], ['column1', 'column3', 'column5', 'column9', 'column10', 'column14'], ['mob no'], ['aaria jain'], ['cust_address1', 'cust_address2', 'cust_address3'], ['cust_zip'], ['dealer', 'dealercity'], ['model', 'car model'], ['variant'], ['colour'], ['external_id'], ['cust_phone1', 'cust_phone2'], ['segment'], ['statement_to_email'], ['cust_email'], ['cust_bank_acc_num', 'cust_bank_acc_name', 'alt_bank_acc_num'], ['bank_agency_code'], ['dispatch_mode'], ['daily_status'], ['remittance_center'], ['rateplan'], ['imsi'], ['balance'], ['subnores'], ['hub', 'hubli'], ['last_billamt'], ['aon'], ['asd'], ['zone'], ['arpu'], ['bucket'], ['invamt_recent', 'invamt_secondrecent', 'invamt_thirdrecent'], ['nbp'], ['zip code', 'f code'], ['ownernumber'], ['salutation'], ['product owned'], ['season owned'], ['apartment owned'], ['payment plan'], ['sales branch'], ['reporting branch'], ['channel', 'channel code'], ['sales exec'], ['persons name'], ['cell phone '], ['party name'], ['country code', 'country code 2', 'country code  mob1', 'country code mob2', 'country code fax'], ['area code', 'area code 2', 'area code fax'], ['customer id', 'customer details'], ['dme code', 'smcode', 'se code'], ['de code/ se code'], ['promo code'], ['branch code'], ['dip location'], ['existing /new customer'], ['salary/self employed'], ['cat a/b companies'], ['bt'], ['add-on'], ['insurance(y/n)'], ['billpay(y/n)'], ['dipstatus(y/n/i)'], ['returndate'], ['resubmission date', 'resubmissionreturndate'], ['cat'], ['sic_code'], ['login id', 'login id _1'], ['ip city'], ['page graph'], ['name on page'], ['sms alert no'], ['reason'], ['myid'], ['customer details_1'], ['status_1', 'status_2'], ['nam_ful'], ['pho_off2'], ['citycode'], ['res number'], ['post'], ['status date', 'statustype'], ['res_ph1'], ['card type'], ['type of sale'], ['tariff plan'], ['tse'], ['std code_1', 'std code_2'], ['co-code'], ['cus name'], ['mobi'], ['date of submission'], ['mobile','mobile-1', 'mobile-2', 'mobile-3', 'mobile-4', 'mobile-5','mobilenumber', 'mobile number', 'mobile no_', 'mobile2', 'mobile no', 'mobileno', 'mobile3', 'mobile1', 'mobile +', 'mobile 3', 'mobile 4', 'mobile 1', 'mobile 2', 'mobile 5','contact phone no_(mobile)'], ['credit card'], ['premium'], ['ph no'], ['hypoth'], ['s_ no_'], ['school'], ['ptc'], ['teliphone1', 'teliphone2', 'teliphone3'], ['cetegry'], ['wibeside'], ['additionalemail id', 'additional email id'], ['fn'], ['ln'], ['office name'], ['office # (1)', 'office # (2)', 'office # (3)'], ['ext #'], ['domain'], ['# of employees'], ['job function 2'], ['revenue'], ['linkedin link'], ['company link'], ['job_title'], ['user_company_domain'], ['user_other_email', 'seller_email'], ['principal'], ['category_name'], ['address_state'], ['roll_no', 'roll no'], ['d_birth'], ['edu_'], ['ac_no'], ['slnoinpart'], ['house_no', 'house_no_e', 'house_no_uni'], ['section_no', 'section_nm_en', 'section_nm_v'], ['rln_fm_nm', 'rln_fm_nm_e', 'rln_fm_nm_uni'], ['fm_name_uni'], ['ac_nm_en'], ['tehsil_nm_en', 'tehsil_nm_v'], ['ps_building'], ['fvtm_name'], ['full address'], ['profession'], ['bill cycle', 'ioip bill cycle'], ['authorized signatory 1 name', 'authorized signatory 1 number'], ['account billing address'], ['date and time of appr_ from da', 'date and time of fa accept', 'date and time of pv accept'], ['fa user id', 'lv user id', 'pv user id'], ['date and time of lv accept'], ['dedup count'], ['blacklist count'], ['number category'], ['number charges'], ['invoice date'], ['not activated'], ['score'], ['dash', 'dash_1'], ['name_1'], ['fax/tel_'], ['year of passing'], ['name  & com'], ['clients'], ['potential client']]
    dictionary={}
    for i in range(0,len(outer_elements)):
        inner_element=outer_elements[i]
        for j in range(0,len(inner_element)):
            dictionary[inner_element[j]]=inner_element[0]
    print(dictionary)

    f=open('headers_clustered.json','w')

    f.write(json.dumps(dictionary))
    print("Ended")
        

    