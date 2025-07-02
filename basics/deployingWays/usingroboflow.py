from roboflow import Roboflow
from dotenv import load_dotenv
import os
load_dotenv()

key =  os.getenv('ROBOFLOW_API_KEY')
rf = Roboflow(api_key = key)
workspace = rf.workspace("jonathan-jkoju")

workspace.deploy_model(
  model_type="yolov8",
  model_path="D:/cmputerVisionSimform/TrainedYoloModel/kaggle/working/my_model/train",
  project_ids=["wastedetector-5ww2z"],
  model_name="murial"
)