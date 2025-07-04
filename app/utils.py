from datetime import datetime

def format_timestamp(ts):
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y - %I:%M %p UTC")

def format_event(data, event_type):
    if event_type == "push":
        return {
            "author": data["pusher"]["name"],
            "type": "push",
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": format_timestamp(data["head_commit"]["timestamp"])
        }

    elif event_type == "pull_request":
        pr = data["pull_request"]
        return {
            "author": pr["user"]["login"],
            "type": "pull_request",
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": format_timestamp(pr["created_at"])
        }

    elif event_type == "merge":
        # Optional, if your GitHub event includes merge info
        pass

    return None
