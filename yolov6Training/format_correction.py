import json

# Load prediction and GT data
with open("D:/yolov6 results/predictions.json", "r") as f:
    predictions = json.load(f)

with open("C:/Users/TEJAS/Downloads/test_coco_gt.json", "r") as f:
    coco_gt = json.load(f)

# Build a mapping: filename (without .jpg) -> image_id
filename_to_id = {
    img["file_name"].replace(".jpg", ""): img["id"] for img in coco_gt["images"]
}

# Fix prediction image_ids
fixed_predictions = []
for pred in predictions:
    img_key = pred["image_id"]
    if img_key in filename_to_id:
        pred["image_id"] = filename_to_id[img_key]
        fixed_predictions.append(pred)
    else:
        print(f"Skipping unmatched prediction: {img_key}")

# Save to new file
with open("./predictions_fixed.json", "w") as f:
    json.dump(fixed_predictions, f)

print("✅ Fixed predictions saved as predictions_fixed.json")
