import common
import sys, getopt

def main(argv):
   minknow_directory = ''
   output_directory = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('Usage: \"main.py -i <minknow_directory> -o <output_directory>\"')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('Usage: \"main.py -i <minknow_directory> -o <output_directory>\"')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         minknow_directory = arg
      elif opt in ("-o", "--ofile"):
         output_directory = arg
   print ('MinKnow Directory is "', minknow_directory)
   print ('Output directory is "', output_directory)
if __name__ == "__main__":
   main(sys.argv[1:])

def minknow_pipeline():
    common.directory_scan()