# qgis2sketchfab
Code and notes to export 3D models from QGIS and import into Sketchfab

## Intro
These are the steps I have used to export a 3D model from QGIS using the qgis2threejs plugin, and upload the model to Sketchfab.  Please note I am not an expert in 3D, and have achieved this workflow through trial and error and a lot of Googling.  The workflow might not be applicable for other data scenarios, and has not been thoroughly tested.  I would welcome suggestions and improvements, particularly in the generation of normals.  Ideally the export from qgis2threejs would support all the features needed in the 3D file so it could be uploaded directly to Sketchfab without the need for tweaking.

## Steps
### Export .obj file from qgis2threejs
