import h5py, sys, getopt
from matplotlib import pyplot as plt

def compare_hdf(file1,file2,dset):
    f1=h5py.File(file1, 'r')
    f2=h5py.File(file2, 'r')
    d1=f1[dset].value
    d2=f2[dset].value
    return d1-d2
    
def show_2d_arr(array):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(array)
    plt.show()

def main(argv):
    firstfile = ''
    secondfile = ''
    dsetcompare = ''
    try:
        opts, args = getopt.getopt(argv,"hi:j:c:",["firstfile=","secondfile=","dsetcompare="])
    except getopt.GetoptError:
        print 'compare_hdf.py -i <firstfile> -j <secondfile> -c <dset2compare>'
        sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
          print 'compare_hdf.py -i <firstfile> -j <secondfile> -c <dset2compare>'
          sys.exit()
      elif opt in ("-i", "--firstfile"):
          firstfile = arg
      elif opt in ("-j", "--secondfile"):
          secondfile = arg
      elif opt in ("-c","--dsetcompare"):
          dsetcompare = arg
    print 'The first file is "', firstfile
    print 'The second file is "', secondfile
    print 'The dataset to compare is "', dsetcompare

    image=compare_hdf(firstfile,secondfile,dsetcompare)
    show_2d_arr(image)


if __name__ == "__main__":
    main(sys.argv[1:])
