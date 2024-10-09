import random
from rdkit import Chem
from rdkit.Chem import AllChem

class MoleculeGenerator:
    def __init__(self):
        # 定义可用的原子类型
        self.atoms = ['C', 'N', 'O', 'F', 'Cl', 'Br']
    
    def generate_molecule(self):
        # 这是一个非常简单的随机分子生成器
        # 实际的AI药物设计会使用更复杂的模型,如VAE或GAN
        
        # 随机决定分子中的原子数量
        num_atoms = random.randint(5, 15)
        mol = Chem.RWMol()
        
        # 添加原子
        for _ in range(random.randint(5, 10)):
            mol.AddAtom(Chem.Atom(6))  # 添加碳原子
        
        # 添加键
        for _ in range(random.randint(4, 9)):
            i = random.randint(0, mol.GetNumAtoms() - 1)
            j = random.randint(0, mol.GetNumAtoms() - 1)
            if i != j and not mol.GetBondBetweenAtoms(i, j):
                mol.AddBond(i, j, Chem.BondType.SINGLE)
        
        # 转换为RDKit分子对象并进行清理
        mol = mol.GetMol()
        Chem.SanitizeMol(mol)
        
        # 返回分子的SMILES表示
        return Chem.MolToSmiles(mol)