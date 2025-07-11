import json

with open("C:/Users/TEJAS/Downloads/test_coco_gt.json", "r") as f:
    data = json.load(f)

# If "info" is missing, add it
if "info" not in data:
    data["info"] = {"description": "Patched info field for compatibility"}

# Save patched file
with open("./test_coco_gt_patched.json", "w") as f:
    json.dump(data, f)

print("✅ Patched and saved as test_coco_gt_patched.json")
