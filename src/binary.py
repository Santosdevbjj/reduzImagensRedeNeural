"""
binary.py
Binariza uma imagem em tons de cinza (0 ou 255), usando threshold fixo ou método de Otsu.
"""

import sys
from pathlib import Path
import numpy as np
from PIL import Image
from skimage.filters import threshold_otsu

def to_binary(input_gray_path: Path, output_path: Path, threshold: int = None):
    img = Image.open(str(input_gray_path)).convert("L")
    arr = np.array(img, dtype=np.uint8)

    if threshold is None:
        th = threshold_otsu(arr)
        print(f"Threshold Otsu calculado: {th}")
    else:
        th = threshold
        print(f"Threshold fixo usado: {th}")

    binary = np.where(arr > th, 255, 0).astype(np.uint8)
    Image.fromarray(binary, mode="L").save(str(output_path))
    print(f"Imagem binarizada salva em: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Uso: python binary.py <input_gray> <output_binary> [threshold]")
        sys.exit(1)

    input_gray_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    threshold = int(sys.argv[3]) if len(sys.argv) == 4 else None
    to_binary(input_gray_path, output_path, threshold)
