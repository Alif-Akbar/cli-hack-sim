"""
@author: Abdullah Affandi
Implementasi Queue Traffic berdasarkan traffic.json
"""

import json
from pprint import pformat

from DSA.queue.queue import Queue


class TrafficQueue(Queue):
    """
    TrafficQueue mewarisi Queue.

    Method asli dari Queue yang tetap dipakai:
    - enqueue()
    - dequeue()
    - front()
    - is_empty()
    - size()

    Method tambahan di class ini hanya untuk kebutuhan traffic:
    - load_from_json()
    - display()
    - display_front()
    - display_dequeue()
    """

    # TODO: Please butuh filehandler untuk load json :/
    def load_from_json(self, file_path: str) -> None:
        """
        Membaca traffic.json lalu memasukkan setiap request traffic ke queue.
        """

        with open(file_path, "r", encoding="utf-8") as file:
            traffic_data = json.load(file)

        for server_name, monitors in traffic_data.items():
            for monitor_name, traffic_logs in monitors.items():
                for traffic in traffic_logs:
                    item = {
                        "traffic_id": traffic.get("request_id"),
                        "monitor_id": monitor_name,
                        "server_id": server_name,
                        "metadata": {
                            "timestamp": traffic.get("timestamp"),
                            "method": traffic.get("method"),
                            "url": traffic.get("url"),
                            "source": traffic.get("source"),
                            "destination": traffic.get("destination"),
                            "protocol": traffic.get("protocol"),
                            "status": traffic.get("status"),
                            "payload": traffic.get("payload"),
                            "latency": traffic.get("latency"),
                            "threat_level": traffic.get("threat_level"),
                        },
                    }

                    self.enqueue(item)

    def display(self) -> None:
        if self.is_empty():
            print("Queue traffic kosong.")
            return

        nodes = []

        for item in self.queue:
            metadata = item["metadata"]

            text = (
                f"[{item['traffic_id']}]\n"
                f" monitor_id : {item['monitor_id']}\n"
                f" server_id  : {item['server_id']}\n"
                f" method     : {metadata.get('method')}\n"
                f" url        : {metadata.get('url')}\n"
                f" status     : {metadata.get('status')}\n"
                f" latency    : {metadata.get('latency')}"
            )

            nodes.append(text)

        print("\n -> \n".join(nodes))

    def display_front(self) -> None:
        if self.is_empty():
            print("Queue traffic kosong.")
            return

        item = self.front()

        print("+=======================================================+")
        print("|                    FRONT TRAFFIC                      |")
        print("+=======================================================+")
        print(f" Traffic ID : {item['traffic_id']}")
        print(f" Monitor ID : {item['monitor_id']}")
        print(f" Server ID  : {item['server_id']}")
        print("+=======================================================+")
        print(" Metadata:")
        print(pformat(item["metadata"], indent=4, width=60))
        print("+=======================================================+")

    def display_dequeue(self) -> None:
        if self.is_empty():
            print("Queue traffic kosong.")
            return

        item = self.dequeue()

        print("+=======================================================+")
        print("|                  DEQUEUE TRAFFIC                      |")
        print("+=======================================================+")
        print(f" Traffic ID : {item['traffic_id']}")
        print(f" Monitor ID : {item['monitor_id']}")
        print(f" Server ID  : {item['server_id']}")
        print("+=======================================================+")
        print(" Metadata:")
        print(pformat(item["metadata"], indent=4, width=60))
        print("+=======================================================+")
        print(f" Sisa Queue : {self.size()}")
