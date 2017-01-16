# qgis2sketchfab
Code and notes to export 3D models from QGIS and import into Sketchfab

## Intro
These are the steps I have used to export a 3D model from QGIS using the qgis2threejs plugin, and upload the model to Sketchfab.  Please note I am not an expert in 3D, and have achieved this workflow through trial and error and a lot of Googling.  The workflow might not be applicable for other data scenarios, and has not been thoroughly tested.  I would welcome suggestions and improvements, particularly in the generation of normals.  Ideally the export from qgis2threejs would support all the features needed in the 3D file so it could be uploaded directly to Sketchfab without the need for tweaking.

If you find this workflow useful, I would appreciate a mention:  Mike Gill, Avon Valley Archaeological Society.

## Requirements
* Python.  The script has been run with Python 2.7, but may work with other versions
* MeshLab

## Steps
### Export .obj file from qgis2threejs
1.  In QGIS, open the qgis2threejs dialogue.  For the 'Template file' in the top drop-down, choose FileExport.html.
2.  Configure the settings for the model in the dialogue, then click Run.  Note - I had some problems trying to export very large models.
3.  A web browser should appear, with buttons for saving different 3D models.  In the 'Save all layers' section, click the 'Wavefront (.obj)' button.  Be patient.  After a short time, you should be prompted to save a zip file.  Save this to disk.
4.  Now click on the 'Wavefront material library (.mtl)' button  When prompted to save, give the zip a different name and save to the same folder.
5.  Extract all the files from the two zips to the containing folder.  Note - an identical PNG file is contained in each zip.

### Edit the .obj / .mtl files
**Note - for the remaining steps, ignore the files which include '\_sides' in their name**

1.  Open the .mtl file and add the following line to the end:

   `map_Kd <png file name>`

   substituting `<png file name>` with the name of the .png file that was extracted from the zip.  For example:

   `map_Kd 0_old-sarum-1m-grid-ascii_0.png`

2.  Clone or download this Git repo using a Git client, or by using the 'Clone or download' button in Github.
3.  There is a Python script which will add uv coordinates to the .obj file, writing out a new file.  Run the python script in the cloned / downloaded repository as follows:

   `python create_uv_coords.py <in filename> <out filename>`
   
   For example:
   
   `python create_uv_coords.py model.obj model_with_uv.obj`
   
   You can use relative or full path names as part of the filename parameters, but remember to wrap them in double quotes if they have spaces in.
   
### Flip normals in MeshLab
The .obj file produced by the previous process appears to be lit from the wrong side if uploaded to Sketchfab.  I used MeshLab to fix this - I welcome any tips on how this could be achieved in the Python script.

1.  Open MeshLab, then File > Import Mesh.  Choose the .obj file specified as the out filename when running the python script.
2.  After a while, the model should appear, with a texture, but lit from the underneath.
3.  Click the 'Select faces in a rectangular region' tool and drag a box around the entire mesh.  It should turn red showing all the faces have been selected.
4.  In the menu, choose Filters > Normals, Curvature and Orientation > Invert Faces Orientation.  In the dialogue that appears. click Apply and then Close.
5.  Click the 'Select faces in a rectangular region' tool and drag a box away from the mesh to deselect the faces.  Click the tool again to deselect the tool.  The model should now be correctly lit.
6.  Export the model as follows:  File > Export Mesh As.  For 'Files of Type', choose 'Alias Wavefront Object (\*.obj)'.  Specify a different name to the original, and click 'Save'.  On the dialogue that appears, make sure the 'Normal' option is ticked.  Click OK.

### Zip files and upload to Sketchfab
1.  Zip up the .obj file and .mtl file exported from Meshlab, and the original .png file into a single zip archive.
2.  Upload this file to Sketchfab.


