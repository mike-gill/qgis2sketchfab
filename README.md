# qgis2sketchfab
Code and notes to export 3D models from QGIS and import into Sketchfab

## Intro
These are the steps I have used to export a 3D model from QGIS using the qgis2threejs plugin, and upload the model to Sketchfab.  Please note I am not an expert in 3D, and have achieved this workflow through trial and error and a lot of Googling.  The workflow might not be applicable for other data scenarios, and has not been thoroughly tested.  I would welcome suggestions and improvements, particularly in the generation of normals.  Ideally the export from qgis2threejs would support all the features needed in the 3D file so it could be uploaded directly to Sketchfab without the need for tweaking.

## Steps
### Export .obj file from qgis2threejs
1.  In QGIS, open the qgis2threejs dialogue.  For the 'Template file' in the top drop-down, choose FileExport.html.
2.  Configure the settings for the model in the dialogue, then click Run.  Note - I had some problems trying to export very large models.
3.  A web browser should appear, with buttons for saving different 3D models.  In the 'Save all layers' section, click the 'Wavefront (.obj)' button.  Be patient.  After a short time, you should be prompted to save a zip file.  Save this to disk.
4.  Now click on the 'Wavefront material library (.mtl)' button and save the zip to the same folder.

