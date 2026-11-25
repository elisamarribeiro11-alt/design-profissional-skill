import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'design-profissional'
if not SKILL.exists():
    SKILL = Path.home() / '.codex/skills/remote-skills/skill-6b034e2750448191b7af2f968dc9b35f'

class QualidadeComercial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.main = (SKILL / 'SKILL.md').read_text()
        cls.ref = (SKILL / 'references/qualidade-comercial.md').read_text()
        cls.rubric = (SKILL / 'references/auditoria-visual.md').read_text()
        cls.report = (SKILL / 'assets/relatorio-auditoria.md').read_text()

    def test_all_criteria_are_audited_and_reported(self):
        for criterion in ['Domínio', 'Ícones', 'Favicon', 'Identidade', 'Espaçamento', 'Selos', 'Teclado virtual', 'Documentos', 'Promessas', 'Avaliações', 'Enumeração']:
            with self.subTest(criterion=criterion):
                self.assertIn('| ' + criterion, self.ref)
                self.assertIn('| ' + criterion, self.report)

    def test_all_three_modes_and_read_only_audit(self):
        for mode in ['`criar`', '`melhorar`', '`auditar`']:
            self.assertIn(mode, self.main.split('## Controle obrigatório')[1].split('## Referências')[0])
        self.assertIn('somente leitura', self.main.split('## Controle obrigatório')[1])

    def test_blockers_and_evidence_gate(self):
        for term in ['avaliações falsas', 'promessas enganosas', 'formulário essencial', 'violação de privacidade']:
            self.assertIn(term, self.rubric.lower())
        self.assertIn('NV em verificação obrigatória impede aprovação global', self.rubric)
        self.assertIn('não declare aprovação global', self.main)

    def test_exceptions_and_device_limits(self):
        for term in ['aprovação do cliente', 'Logotipo tipográfico', 'atribuições obrigatórias', 'sequência lógica', 'Android e iOS', 'não comprova', 'revisão jurídica']:
            self.assertIn(term, self.ref)

    def test_existing_rubric_kept(self):
        for dimension in ['Layout', 'Alinhamento', 'Hierarquia', 'Proximidade', 'Equilíbrio', 'Consistência', 'Cores', 'Contraste', 'Espaçamento', 'Usabilidade', 'Responsividade', 'Acessibilidade', 'Qualidade das animações', 'Desempenho']:
            self.assertIn('| ' + dimension + ' |', self.rubric)
        for severity in ['Crítico', 'Alto', 'Médio', 'Baixo']:
            self.assertIn(severity, self.rubric)

if __name__ == '__main__':
    unittest.main()
