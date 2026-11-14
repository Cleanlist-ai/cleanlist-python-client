"""A live call without commit answers with a LivePreview whose committed is
false. It used to fail to decode: the generator turned the boolean const into
a string enum that only accepted 'false'."""

from cleanlist_ai.aio.models.live_preview import LivePreview as AsyncLivePreview
from cleanlist_ai.models.live_preview import LivePreview

PREVIEW = {
    "committed": False,
    "action": "agents.set_status",
    "description": "Turn the agent on.",
    "credits_max": 12.5,
    "effects": ["sends", "crm_writes"],
    "required_scopes": ["agents:write"],
    "missing_scopes": [],
    "estimate": {"credits": 12.5},
}


def test_a_live_preview_decodes_with_committed_false():
    for model in (LivePreview, AsyncLivePreview):
        preview = model.from_dict(PREVIEW)
        assert preview.committed is False
        assert preview.effects == ["sends", "crm_writes"]
