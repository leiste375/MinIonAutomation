import common
import sys, getopt

def minknow_pipeline(m_dir):
    common.directory_scan(input_dir=m_dir)
    
def main(argv):
   minknow_directory = ''
   output_directory = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('Usage: \"main.py -i <minknow_directory> -o <output_directory>\"')
      sys.exit(2)
   for opt, arg in opts:
        match opt:
            case '-h':
                print ('Usage: \"main.py -i <minknow_directory> -o <output_directory>\"')
                sys.exit()
            case '-i':
                minknow_directory = arg
            case '-o':
                output_directory = arg
   print (f'MinKnow Directory is {minknow_directory}')
   print (f'Output directory is {output_directory}')
   minknow_pipeline(minknow_directory)
if __name__ == "__main__":
   main(sys.argv[1:])