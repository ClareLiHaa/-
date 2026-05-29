import os
import sys

def find_node():
    # Check common locations
    common_paths = [
        r"C:\Program Files\nodejs",
        r"C:\Program Files (x86)\nodejs",
        os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "npm"),
        os.path.join(os.path.expanduser("~"), "nodejs"),
        r"C:\nodejs",
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            print(f"Checking: {path}")
            for file in os.listdir(path):
                if file.lower() == "node.exe":
                    node_path = os.path.join(path, file)
                    print(f"Found node.exe: {node_path}")
                    return node_path
    
    # Check PATH
    print("\nChecking PATH environment variable:")
    for path_dir in os.environ["PATH"].split(os.pathsep):
        if path_dir and os.path.exists(path_dir):
            node_exe = os.path.join(path_dir, "node.exe")
            npm_cmd = os.path.join(path_dir, "npm.cmd")
            if os.path.exists(node_exe):
                print(f"Found in PATH: {node_exe}")
                return node_exe
    
    return None

if __name__ == "__main__":
    node_path = find_node()
    if node_path:
        print(f"\nNode.js found at: {node_path}")
        # Try to find npm
        node_dir = os.path.dirname(node_path)
        npm_path = os.path.join(node_dir, "npm.cmd")
        if os.path.exists(npm_path):
            print(f"npm found at: {npm_path}")
    else:
        print("Node.js not found")
