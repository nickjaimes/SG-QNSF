from .qnsf_memory_engine import QNSFMemoryEngine
from .qnsf_crypto_module import QNSFCryptoModule


class QNSFCore:
    """
    QNSF – Quantum Neuromorphic System Fabric (Core Orchestrator)

    Responsibilities:
    - Receive events from TRINITY, EAGLE EYE, SG SAFECOIN, etc.
    - Store patterns in neuromorphic memory
    - Propose evolved strategies/algorithms
    - Trigger cryptographic metamorphosis when necessary
    """

    def __init__(self):
        self.memory_engine = QNSFMemoryEngine()
        self.crypto_module = QNSFCryptoModule()

    def absorb_event(self, event: dict):
        """
        Ingest an event and send to memory engine.
        Example event:
        {
            "domain": "system|finance|climate|health",
            "result": "success|failure|partial",
            "severity": 0.0 - 1.0,
            "action_taken": "string",
        }
        """
        self.memory_engine.store_event(event)

    def mutate_algorithm(self, algorithm_descriptor: str) -> str:
        """
        Given a basic algorithm descriptor or name, return evolved variant.
        This is conceptual: in real use this might modify real model configs.
        """
        return self.memory_engine.propose_evolved_strategy(algorithm_descriptor)

    def evaluate_risk_trajectory(self) -> float:
        """
        Use stored events to estimate long-range risk.
        Returns risk index (0.0 - 1.0).
        """
        return self.memory_engine.compute_risk_index()

    def check_and_rekey_if_needed(self, last_event: dict):
        """
        Triggers cryptographic re-keying if event severity is high enough.
        """
        if last_event.get("severity", 0) >= 0.85:
            return self.crypto_module.regenerate_keys(reason="high_severity_event")
        return None
