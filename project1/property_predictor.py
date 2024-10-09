from rdkit import Chem
from rdkit.Chem import Descriptors

class PropertyPredictor:
    def predict_properties(self, smiles):
        # 从SMILES创建RDKit分子对象
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return {"错误": "无效的SMILES"}
        
        # 计算并返回各种分子性质
        properties = {
            "分子量": Descriptors.ExactMolWt(mol),
            "LogP": Descriptors.MolLogP(mol),
            "氢键受体数": Descriptors.NumHAcceptors(mol),
            "氢键供体数": Descriptors.NumHDonors(mol),
            "可旋转键数": Descriptors.NumRotatableBonds(mol)
        }
        return properties