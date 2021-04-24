# store to mysql
from filter.feed_filter import FeedFilterRequest

leaf_category_ids = [
	'179413',
	'33545',
	'33543',
	'33544',
	'33546',
	'33547',
	'33548',
	'46094',
	'43946',
	'38634',
	'33551',
	'33550',
	'33552',
	'33553',
	'33554',
	'33555',
	'33556',
	'36474',
	'42604',
	'33557',
	'33558',
	'33560',
	'173511',
	'33561',
	'33562',
	'33563',
	'33564',
	'33565',
	'33566',
	'42605',
	'33567',
	'33568',
	'33569',
	'33570',
	'33571',
	'177698',
	'177697',
	'179846',
	'179847',
	'33575',
	'33578',
	'177700',
	'177699',
	'33577',
	'33595',
	'33596',
	'33598',
	'33597',
	'33600',
	'33601',
	'46095',
	'46096',
	'33602',
	'33603',
	'33604',
	'50447',
	'50449',
	'50446',
	'50448',
	'33643',
	'50451',
	'50452',
	'177702',
	'177704',
	'177705',
	'177707',
	'177706',
	'177703',
	'177708',
	'177709',
	'33606',
	'33607',
	'33609',
	'46097',
	'33610',
	'38656',
	'33613',
	'33614',
	'33615',
	'33616',
	'33617',
	'33619',
	'33620',
	'50454',
	'33622',
	'38657',
	'6778',
	'46098',
	'33623',
	'33624',
	'33625',
	'33626',
	'33627',
	'33621',
	'33629',
	'33632',
	'33633',
	'33630',
	'33634',
	'33635',
	'33636',
	'42610',
	'38658',
	'33639',
	'36475',
	'50457',
	'33640',
	'50456',
	'179849',
	'179851',
	'179850',
	'33644',
	'33645',
	'33646',
	'33648',
	'33649',
	'33654',
	'33650',
	'42611',
	'33651',
	'38659',
	'63688',
	'50455',
	'33638',
	'33652',
	'33647',
	'33653',
	'33655',
	'33656',
	'179852',
	'33657',
	'33659',
	'33660',
	'33661',
	'33663',
	'33662',
	'33665',
	'33666',
	'33667',
	'33668',
	'33669',
	'46099',
	'38660',
	'33673',
	'33674',
	'33677',
	'43951',
	'43952',
	'33675',
	'33676',
	'46100',
	'33678',
	'33679',
	'33680',
	'33681',
	'33682',
	'33684',
	'33685',
	'6781',
	'63689',
	'33686',
	'33688',
	'33689',
	'33690',
	'33691',
	'33692',
	'40016',
	'46101',
	'33693',
	'63690',
	'33695',
	'63691',
	'40017',
	'33697',
	'33698',
	'179848',
	'33696',
	'33699',
	'42612',
	'33700',
	'50458',
	'33702',
	'33701',
	'33703',
	'33704',
	'46102',
	'50459',
	'33705',
	'40018',
	'33706',
	'33708',
	'33709',
	'38661',
	'33710',
	'33711',
	'33712',
	'184669',
	'33713',
	'33714',
	'172518',
	'36476',
	'42613',
	'33715',
	'33716',
	'33717',
	'6763',
	'33722',
	'6779',
	'177711',
	'177710',
	'33725',
	'184627',
	'184628',
	'184629',
	'184630',
	'33580',
	'33581',
	'33582',
	'33583',
	'33584',
	'33585',
	'33586',
	'42609',
	'33587',
	'33588',
	'33590',
	'33589',
	'33591',
	'33592',
	'33593',
	'46104',
	'33735',
	'33736',
	'63692',
	'46103',
	'33738',
	'33728',
	'33730',
	'33729',
	'33731',
	'33732',
	'33727',
	'171115',
	'171117',
	'33733',
	'33740',
	'33741',
	'33742',
	'33744',
	'42614',
	'33746',
	'180090',
	'179696',
	'66471',
	'33747',
	'66479',
	'43961',
	'170141',
	'33749',
	'122154',
	'43953'
]

feed_filter_obj = FeedFilterRequest(input_file_path='./output-1-0.gz')
file_path = feed_filter_obj.store_mysql(leaf_category_ids=leaf_category_ids)