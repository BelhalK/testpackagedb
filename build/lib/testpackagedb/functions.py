import os

def get_dbutils(spark):
        try:
            from pyspark.dbutils import DBUtils
            dbutils = DBUtils(spark)
        except ImportError:
            import IPython
            dbutils = IPython.get_ipython().user_ns["dbutils"]
        return dbutils

def AddNumbers(i, j):
    return i + j

def SubtractNumbers(i, j):
    return i - j

def MultiplyNumbers(i, j):
    return i * j


def loadmodel(modelname='search_relevance_v0'):
	dbutils = get_dbutils(spark)
	
	bimodel_finetuned = "s3://nikeplus-ngap-test/bernardabayowa/{}/models/2023-02-03/".format(modelname)
	local_bimodel_path='/tmp/bimodel_finetuned/'

	bimodel_finetuned_cmd="aws s3 cp {} {} --acl bucket-owner-full-control --recursive".format(bimodel_finetuned, local_bimodel_path)
	os.environ['bimodel_finetuned_cmd']=bimodel_finetuned_cmd

	dbutils.fs.mkdirs("file:"+local_bimodel_path)
	return local_bimodel_path