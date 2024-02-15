import subprocess
import hylite
import numpy as np
from hylite import HyData, HyImage, HyCloud, HyLibrary, HyHeader, HyCollection, HyScene
from hylite import io

#
import glob
from PyQt5.QtWidgets import QFileDialog, QMessageBox

try:
    import hylite

    print("websockets is available")
except:
    subprocess.run("pip install hylite")
    print("websockets was not available")


def select_folder(self):
    """
    This function return the project folder directory, in which the json and python script will be saved.
    Here, the user will be ask to search their data directory and select its folder.
    """
    self.folder_name = self.sender().objectName()
    self.project_dir = QFileDialog.getExistingDirectory(
        self.FolderSearch_Button,
        "Select folder ",
        "",
    )
    self.SearchFolder.setText(self.project_dir)
    # print("project directory: ", self.project_dir)
    return self.project_dir


def load_the_data(self):
    """
    This function load the file and return a dictionary
    data_flag :: data file extension
    """
    list_of_files = [a for a in glob.glob(str(self.project_dir) + "/*")]

    try:
        list_hdr = [a for a in list_of_files if ".hdr" in str(a)]
    except:
        pass
    try:
        list_ply = [a for a in list_of_files if ".ply" in str(a)]
    except:
        pass
    try:
        file_dict = dict(
            zip(["ply-file_path:", "hdr-file_path:"], [list_ply, list_hdr])
        )
        print(file_dict)
    except:
        pass

    return file_dict

    # list_data = []
    # if data_flag == '.hdr':
    # 	# open an ENVI image
    # 	image = io.load( r'C:\Users\00110138\OneDrive - The University of Western Australia\HyperSpectral\qgis_hyper\test_data\image.hdr' )
    #     list_data.append(image)
    # elif data_flag =='.ply':
    # 	# open a .ply point cloud
    # 	cloud = io.load( r'C:\Users\00110138\OneDrive - The University of Western Australia\HyperSpectral\qgis_hyper\test_data\hypercloud.ply' )
    #     list_data.append(cloud)
    # else:
    #     pass
    # return  file_dict# list_data.append

    # def describe_data(self,user_name):
    # 	'''
    #     This function describe the cloud data and return a list of infos
    #     # user_name:  your first name
    # 	'''
    # 	cloud.decompress() # this was compressed from float to integer to save space; so we need to convert it back
    # 	#print the data
    # 	cloud.header.print()
    # 	#
    # 	#access data stored in the header file. Note that this is a string.
    # 	print(cloud.header['bands'], type(cloud.header['bands']))
    # 	assert int(cloud.header['bands']) == cloud.band_count() # check value in header matches number of bands in dataset
    # 	##
    # 	print(cloud.header['samples'], type(cloud.header['samples']))

    # 	##
    # 	# get a list from the header file as a numpy array
    # 	wav = cloud.header.get_list('wavelength')
    # 	print("Hyperspectral bands range from: %s nm - %s nm" %( np.min(wav), np.max(wav)) )

    # 	# get camera pose information from the header file
    # 	cam = cloud.header.get_camera(0)
    # 	print("Sensor position is [%.1f,  %.1f,  %.1f] m" % tuple(cam.pos))

    # 	# Add some random information to the header
    # 	cloud.header['myname'] = str(user_name)
    # 	cloud.header['wavenumber'] = 1. / (wav*1e-7)
    # 	# print all infos
    # 	cloud.header.print()
    # 	list_of_describe =[cloud.header.print(),cloud.header['bands'], type(cloud.header['bands']),cloud.header['samples'], type(cloud.header['samples']),"Hyperspectral bands range from: %s nm - %s nm" %( np.min(wav), np.max(wav)),"Sensor position is [%.1f,  %.1f,  %.1f] m" % tuple(cam.pos),cloud.header['myname'],cloud.header['wavenumber'],cloud.header.print()]
    #     return list_of_describe
    # 	#
    # def suite():
    # 	print(cloud.data.shape, "= (pointID, bandID)")
    # 	print(image.data.shape, "= (x,y,bandID)")
    # 	image.data[ np.isnan( image.data ) ] = 0 # data arrays can be directly modified. Do this with care!

    # 	#
    # 	print("Index of 2200. nanometers in hypercloud:", cloud.get_band_index(2200.0))
    # 	#
    # 	print("Index of 2200. nanometers in image:", image.get_band_index(2200.0))
    # 	#
    # 	print( image.get_wavelengths()[18])

    # 	#
    # 	print( "Provided wavelengths must be within %.1f nm of existing bands." % hylite.band_select_threshold )
    # 	#image.get_band_index( 2410. ) # throws an error
    # 	hylite.band_select_threshold = 20
    # 	image.get_band_index( 2410. ) # does not throw an error

    # 	#
    # 	print("Point #10 colour: ", cloud.rgb[10,:])
    # 	print("Point #10 normal: ", cloud.normals[10,:])
    # 	print("Point #10 position: ", cloud.xyz[10,:])

    # 	#
    # 	print( hylite.SWIR ) # some preset bands for false-colour visualisation with SWIR data. Note the floating point.
    # 	#
    # 	fig,ax = image.quick_plot(hylite.SWIR)
    # 	fig.show()
    # 	#
    # 	fig,ax = image.quick_plot( 0, cmap='coolwarm' ) # plot with band index
    # 	fig.show()

    # 	#
    # 	fig,ax = image.quick_plot( 2340., cmap='coolwarm' ) # plot with wavelength
    # 	fig.show()
    # 	#
    # 	fig,ax = cloud.quick_plot('rgb', cloud.header.get_camera(0), fill_holes=True)
    # 	fig.show()

    # 	#
    # 	fig,ax = cloud.quick_plot('klm',cloud.header.get_camera(0), fill_holes=True)
    # 	fig.show()

    #


#     fig, ax = cloud.quick_plot(hylite.SWIR, cloud.header.get_camera(0), fill_holes=True)
#     fig.show()

#     # plot a basic spectral caterpillar
#     fig, ax = cloud.plot_spectra(
#         indices=[108113, 82475, 326198], colours=["r", "g", "b"]
#     )
#     fig.show()

#     #
#     # plot image and associated spectra
#     pixels = [(50, 30), (150, 30), (230, 30)]

#     import matplotlib.pyplot as plt

#     fig, ax = plt.subplots(1, 2, figsize=(18, 5))
#     image.quick_plot(
#         hylite.SWIR, ax=ax[0], ticks=True
#     )  # plot image to existing axes object, and plot x- and y- coords
#     ax[0].scatter([p[0] for p in pixels], [p[1] for p in pixels], color=["r", "g", "b"])

#     # add a spectral caterpillar
#     image.plot_spectra(
#         band_range=(2100.0, 2400.0), indices=pixels, colours=["r", "g", "b"], ax=ax[1]
#     )
#     fig.show()

#     #
#     lib = io.load("test_data/library.csv")
#     fig, ax = lib.quick_plot(band_range=(2000.0, 2500.0))
#     fig.show()

#     # Saving the results
#     # io.save?
#     out = image.copy()  # make a copy of the dataset as otherwise we modify it inplace
#     out.data = 1.0 - image.data  # apply some voodoo magic

#     # save our processed dataset
#     io.save(
#         r"C:\Users\00110138\OneDrive - The University of Western Australia\HyperSpectral\qgis_hyper/outputs/rocks.hdr",
#         out,
#     )

#     #
#     from hylite import HyCollection

#     # initialise a collection
#     C = HyCollection("MyCollection", "./outputs")

#     # put some data in it
#     C.image = image
#     C.image_adj = out
#     C.cloud = cloud
#     C.random_array = np.random.rand(100)  # N.B. this will be stored as an .npy file
#     C.magicvalue = 42  # N.B. this will be stored in the HyCollection's header file
#     C.astring = "foo"  # And so will this

#     # save everything!
#     C.save()  # n.b. you can also save a collection to a different folder using io.save('somepath', C)

#     ##
#     C2 = io.load("./outputs/MyCollection.hdr")
#     #
#     C2.print()  # see what is in this collection, and note that no data has actually been loaded yet
#     ##
#     # access an attribute (and load it into memory)
#     fig, ax = C2.image_adj.quick_plot(hylite.SWIR)
#     fig.show()

#     #
#     C2.print()  # the image has now been loaded into RAM


# return
