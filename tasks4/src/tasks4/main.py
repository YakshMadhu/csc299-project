import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    # Load the API key from your .env file
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("❌ No OPENAI_API_KEY found in .env file.")

    # Initialize the OpenAI client using the loaded key
    client = OpenAI(api_key=api_key)

    # Two long paragraph samples
    paragraph_samples = [
        """Andy Weir’s The Martian is a gripping science-fiction novel that blends realism, science, and human resilience into a survival story set on Mars. It follows astronaut Mark Watney, a botanist and mechanical engineer who becomes stranded on the red planet after a disastrous mission. During a powerful dust storm, the crew of NASA’s Ares III mission is forced to abort. Watney is struck by debris and presumed dead, so his crewmates evacuate and begin the long journey back to Earth—leaving him behind.

When Watney regains consciousness, he realizes he is alone, injured, and without any way to contact Earth. His only chance of survival lies in using his scientific knowledge and the limited supplies left at the Hab—the crew’s habitat. His first major problem is food. With only enough rations for a few months, Watney devises a clever plan: he will grow potatoes using Martian soil, fertilized by his own waste and watered through a risky chemical reaction that generates hydrogen and oxygen. His humor and determination shine even in moments of despair, often using sarcasm to mask fear.

Meanwhile, on Earth, NASA discovers through satellite images that Watney is alive. The news sparks both relief and urgency. The team back home races against time to reestablish communication and plan a rescue. They eventually manage to contact him through the Pathfinder probe, a relic from an earlier Mars mission. This rekindles Watney’s hope, but challenges quickly multiply. His crops die when a small tear in the Hab causes a catastrophic decompression, and supplies begin running dangerously low.

NASA engineers, led by Vincent Kapoor and Mindy Park, coordinate with Watney to plan a survival strategy that will last until the next mission, Ares IV, arrives years later. But time and resources are limited. Meanwhile, the Ares III crew aboard their return ship, Hermes, learns that Watney is still alive. Stricken with guilt, they decide—against NASA’s initial orders—to risk their own lives by turning the spacecraft around for a daring rescue.

Watney must reach the Ares IV launch site, nearly 3,200 kilometers away, with a rover modified for long travel. His journey across the barren Martian landscape is perilous. He encounters dust storms, equipment failures, and moments of near-fatal exhaustion. Yet his blend of engineering skill and relentless optimism keeps him moving forward. Each log entry in his journal becomes a testament to human ingenuity and hope.

The final rescue is an intense, nail-biting sequence. As the Hermes crew executes a high-risk maneuver to capture Watney from Mars’ orbit, every calculation and second counts. After multiple near-misses, Commander Melissa Lewis and her team succeed in pulling him aboard, ending his 549 days of isolation.

The Martian is more than a survival tale—it’s a celebration of science, teamwork, and the indomitable human spirit. Watney’s humor, intellect, and willpower demonstrate how even in the most desolate corner of the universe, hope and creativity can keep humanity alive.""",

"""In the year 2154, humanity has ventured far beyond Earth, seeking new worlds and resources. On the distant moon of Pandora, a lush paradise filled with bioluminescent forests and floating mountains, humans have come to mine a rare mineral called unobtanium. The planet’s air is toxic to humans, but it is home to the Na’vi — tall, blue-skinned beings who live in harmony with nature and worship a life-force deity known as Eywa.

To study and interact with the Na’vi, scientists create the Avatar Program, linking human minds to genetically engineered Na’vi bodies called avatars. Jake Sully, a paraplegic former Marine, is chosen to replace his deceased twin brother in the program. Though he lacks scientific training, Jake brings a soldier’s discipline and courage. When he first awakens in his avatar body, he feels an exhilarating sense of freedom—able to run, climb, and breathe in Pandora’s beauty for the first time.

Initially, Jake’s mission is to gather intelligence for the human corporation’s military arm, led by Colonel Miles Quaritch. The colonel promises Jake that if he helps them relocate the Na’vi from their home, which sits atop a valuable mineral deposit, he will get his legs back. However, Jake’s loyalties begin to shift after he becomes lost in the jungle and is rescued by Neytiri, a fierce and compassionate Na’vi warrior. She brings him to her clan, the Omaticaya, where he learns their ways — their language, their bond with the creatures of Pandora, and their spiritual connection to Eywa through the sacred Tree of Souls.

Over time, Jake undergoes a transformation deeper than the physical one. He falls in love with Neytiri and begins to see the world through her eyes. The Na’vi teach him that all living things are connected in a vast web of energy, something humanity has forgotten. But as Jake’s bond with the tribe grows, the humans prepare for war. The corporation, impatient for results, decides to forcibly remove the Na’vi from their land.

When Jake confesses the truth about his original mission, the tribe feels betrayed and casts him out. Soon after, Colonel Quaritch orders a brutal attack, destroying the Na’vi’s Hometree and killing many of their people. Wracked with guilt, Jake turns against his own kind. With the help of the scientists, he permanently transfers his consciousness into his avatar and unites the remaining Na’vi clans to fight back.

The final battle is breathtaking and tragic. With the Na’vi riding banshees across the sky and humans deploying massive war machines, Pandora becomes a battlefield of fire and spirit. Despite being outgunned, the Na’vi prevail through unity and faith in Eywa. Jake defeats Quaritch in a fierce hand-to-hand fight, symbolizing the triumph of life over greed.

In the end, Jake chooses to stay on Pandora forever. His human body dies, but his mind is reborn in his avatar form. With Neytiri by his side, he opens his eyes to a new world — not as a soldier of Earth, but as one of the People of Pandora."""
    ]

    print("Ready to Summarize, Ready to Summarize, Ready....\n")

    # Loop through and summarize each passage
    for i, desc in enumerate(paragraph_samples, start=1):
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "Summarize each task as a short, clear phrase."},
                {"role": "user", "content": desc},
            ],
        )

        summary = response.choices[0].message.content.strip()
        print(f"\nTask {i} summary: {summary}\n{'-'*60}")

if __name__ == "__main__":
    main()
