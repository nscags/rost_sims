from dataclasses import replace
from typing import TYPE_CHECKING, Optional

from bgpy.shared.enums import (
    Prefixes,
    Relationships,
    Timestamps,
)
from bgpy.simulation_framework.scenarios.scenario import Scenario

if TYPE_CHECKING:
    from bgpy.simulation_engine import Announcement as Ann
    from bgpy.simulation_engine import BaseSimulationEngine


class WSScenario(Scenario):
    min_propagation_rounds: int = 2

    def _get_announcements(
        self,
        *,
        engine: Optional["BaseSimulationEngine"] = None,
    ) -> tuple["Ann", ...]:
        anns = list()
        for victim_asn in self.victim_asns:
            anns.append(
                self.scenario_config.AnnCls(
                    prefix=Prefixes.PREFIX.value,
                    next_hop_asn=victim_asn,
                    as_path=(victim_asn,),
                    timestamp=Timestamps.VICTIM.value,
                    seed_asn=victim_asn,
                    recv_relationship=Relationships.ORIGIN,
                )
            )

        return tuple(anns)

    def post_propagation_hook(self, engine=None, propagation_round=0, *args, **kwargs):  # type: ignore
        """Useful hook for post propagation"""

        if propagation_round == 0:
            for victim_asn in self.victim_asns:
                as_obj = engine.as_graph.as_dict[victim_asn]
                as_obj.policy.prep_withdrawal_for_next_propagation(
                    Prefixes.PREFIX.value
                )
