




















# Beyond Accuracy — 100분 확장 발표 대본

본 발표 60장과 부록 4장. 영어 대본은 실제로 읽는 부분이고, 진행 메모와 별도 활동은 읽지 않습니다.

- 영어 대본: **13,087단어**, 150 wpm 기준 **87:15**.
- 별도 활동·화면 조작: **12:45**. 대본 발화 시간과 중복 계산하지 않습니다.
- 계산된 합계: **100:00**. 실제 시간은 발음, 즉석 설명, 청중 반응에 따라 달라집니다.
- 데모는 개념 설명과 병행합니다. CIC 다운로드·전처리·학습은 사전 완료를 전제로 하며 실행 지연을 무제한 기다리지 않습니다.
- 원본 80분 일정은 index-original.html에 보관했습니다. 이 확장본의 시간표는 시작 시각과 무관한 경과 시간입니다.
- 슬라이드에서 N을 누르면 대본을 볼 수 있습니다. 노트 영역을 클릭한 뒤 스크롤할 수 있습니다.

## 진행표

| 장 | 시작 | 배정 | 제목 |
|---:|---:|---:|---|
| 1 | 00:00 | 01:15 | Beyond Accuracy |
| 2 | 01:15 | 01:25 | This model is more confident when it is wrong |
| 3 | 02:40 | 01:24 | How this tutorial runs |
| 4 | 04:04 | 01:22 | Setup — an agent builds the lab while we talk |
| 5 | 05:26 | 01:52 | Three ways to run it — setup & verify |
| 6 | 07:18 | 01:28 | Detection accuracy is a solved-looking problem |
| 7 | 08:46 | 02:15ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅏn,  | The cost of a small false-positive rate |
| 8 | 11:01 | 01:26 | Overconfidence — wrong ≠ uncertain |
| 9 | 12:27 | 01:26 | Shortcut learning — the fingerprint trap |
| 10 | 13:53 | 01:23 | Distribution shift — and the label problem |
| 11 | 15:16 | 01:56 | Is the lab ready? |
| 12 | 17:12 | 01:30 | Meet the dataset (you take it home) |
| 13 | 18:42 | 01:26 | Two detectors, one dataset |
| 14 | 20:08 | 01:28 | What the experiment compares |
| 15 | 21:35 | 01:28 | Confidence & calibration |
| 16 | 23:03 | 01:29 | What miscalibration looks like |
| 17 | 24:32 | 01:26 | Calibration in one confidence bin |
| 18 | 25:59 | 01:30 | Can we fix calibration? — mostly, yes |
| 19 | 27:29 | 01:27 | The catch: calibration is a snapshot |
| 20 | 28:55 | 01:23 | So… is confidence an error signal at all? |
| 21 | 30:19 | 01:38 | Three ways to run it — pick yours |
| 22 | 31:56 | 01:25 | Uncertainty — what kind of "don't know"? |
| 23 | 33:21 | 01:31 | Estimating uncertainty, in practice |
| 24 | 34:52 | 01:28 | A practical proxy: ensemble agreement |
| 25 | 36:20 | 01:30 | Agreement counts votes |
| 26 | 37:50 | 01:30 | The label-free signal menu |
| 27 | 39:20 | 01:34 | Conformal prediction — guarantees, with fine print |
| 28 | 40:53 | 02:08 | Before the result lands… |
| 29 | 43:01 | 01:57 | Demo 1 — confidence vs agreement |
| 30 | 44:59 | 01:29 | What Demo 1 establishes |
| 31 | 46:27 | 01:32 | Demo 2 — can we trust some alerts completely? |
| 32 | 47:59 | 01:40 | Three ways to run it — precision-1.0 gate |
| 33 | 49:39 | 01:27 | Selective prediction & abstention |
| 34 | 51:06 | 02:28 | Precision, coverage, and recall |
| 35 | 53:34 | 01:28 | Why precision 1.0 matters in a SOC |
| 36 | 55:02 | 01:57 | Demo 2 — the trusted zone, measured |
| 37 | 56:59 | 01:59 | A threshold needs an untouched test |
| 38 | 58:58 | 01:27 | Lab 2 — the dataset you all know |
| 39 | 60:25 | 01:27 | The time split is part of the experiment |
| 40 | 61:52 | 01:56 | Dataset → models, live — download · preprocess · train |
| 41 | 63:48 | 01:25 | Demo 3 — then the week goes on |
| 42 | 65:13 | 01:38 | Three ways to run it — the week goes on |
| 43 | 66:51 | 01:29 | Explainability — necessary, not sufficient |
| 44 | 68:20 | 01:28 | Evidence-based verification |
| 45 | 69:48 | 01:58 | Evidence, in action — one flow, audited |
| 46 | 71:46 | 01:28 | Where drift actually comes from |
| 47 | 73:14 | 01:29 | The drift-detection toolbox |
| 48 | 74:43 | 02:02 | Demo 3 — a real collapse, in real silence |
| 49 | 76:45 | 02:57 | Friday, before the labels arrive |
| 50 | 79:41 | 01:30 | Accept / Review / Withhold |
| 51 | 81:11 | 01:29 | Signal → action map |
| 52 | 82:40 | 03:25 | Choose a route and name the evidence |
| 53 | 86:05 | 01:28 | When the AI in your SOC is an LLM |
| 54 | 87:33 | 01:28 | Trusting (the work of) agents |
| 55 | 89:01 | 01:30 | Tune the gate on your own numbers |
| 56 | 90:31 | 01:28 | Deployment checklist |
| 57 | 92:00 | 01:31 | What today's lab does not prove |
| 58 | 93:31 | 03:03 | The whole story, on one screen |
| 59 | 96:34 | 01:44 | Three ways to break the lab (please do) |
| 60 | 98:18 | 01:42 | Take-home |

## 발표 대본

### 01. Beyond Accuracy

진행 00:00–01:15 · 대본 188단어 · 별도 활동 0초

진행 메모: 인사 + 소속 소개. 노트북 화면: 이 슬라이드 + 터미널 준비 상태 확인.

Good morning, everyone. I am Ui-Jun Baek from the Science and Technology Security Research Center at KISTI. Thank you for joining this tutorial on assessing the reliability of AI outputs in security operations.

We often introduce a security model by saying how accurately it classifies traffic. That is a useful starting point. But an analyst receives individual alerts, usually without an immediate answer key, and must decide whether to investigate, block, or wait. Today we will connect model evaluation to that decision.

We will use a small reproducible laboratory, then a traffic dataset with a time-based evaluation. Along the way, I will ask you to interpret the results before I give my interpretation. You can run the examples on your own machine, follow the screen, or take the artifact home.

My aim is that you leave with a way to question a confident prediction. What evidence supports it? What would make us withhold action? And what can we observe when labels are unavailable? Keep those questions in mind even when we discuss unfamiliar terminology. They connect every part of this session, from calibration to the final operational policy.

### 02. This model is more confident when it is wrong

진행 01:15–02:40 · 대본 212단어 · 별도 활동 0초

진행 메모: 청중에게 질문 던지기: "confidence 0.96이면 믿으시겠습니까?" 2~3초 침묵. 이 수치는 오늘 라이브로 재현됨을 예고.

Let us begin with the result that motivated this tutorial. Look at the two rows. The baseline model's mean confidence is about zero point nine four six when its prediction is correct. When its prediction is wrong, the mean is about zero point nine six four. The mistakes are, on average, more confident.

Before I explain the experiment, imagine receiving one of those predictions in an automated response system. The model says attack, and the displayed confidence is ninety-six percent. Would that number alone justify blocking a connection? Think about the distinction between a number that looks like a probability and evidence that a particular action is appropriate.

These are reference results from our controlled synthetic test, whose overall baseline accuracy is about sixty-nine percent. They are not estimates of the failure rate of all intrusion detectors. We deliberately constructed an evaluation that exposes a weakness, and we will reproduce and inspect it in Demo One.

Notice also what the table leaves unanswered. It does not tell us the full distribution of scores, whether a threshold can isolate reliable predictions, or whether the same behavior occurs on another dataset. Those unanswered questions will drive the rest of the tutorial. For now, remember the direction of the difference: confidence increased among the errors.

### 03. How this tutorial runs

진행 02:40–04:04 · 대본 209단어 · 별도 활동 0초

진행 메모: 이중 트랙 + 파이프라인 방식 설명. "제가 에이전트에게 일을 시켜두고, 그동안 개념을 설명합니다."

Here is how we will work through the problem. We start with the traps that make a good evaluation score difficult to translate into a reliable operational decision. Then we build up confidence, calibration, and agreement as quantities we can interpret. The live experiments will let us test specific claims about those quantities.

There are two laboratories. The synthetic laboratory gives us control over the failure mechanism. We know where the misleading feature is because we placed it there. The CIC laboratory gives us a different challenge: models trained on earlier traffic encounter later traffic. The results will complicate the first lab's apparent success.

Each execution page offers three routes. You can ask a coding agent to run the task, use the commands directly, or use the buttons on the local presentation server. Choose one route for each task. Running all three creates duplicate work without giving us a better experiment.

We will start jobs before explaining the concepts they illustrate, so computation can happen while we talk. The pauses in this session are for inspecting results and making decisions, rather than watching a progress bar. At the end, we will turn the observations into an acceptance policy and examine how the same verification habits apply to agent outputs.

### 04. Setup — an agent builds the lab while we talk

진행 04:04–05:26 · 대본 205단어 · 별도 활동 0초

진행 메모: 킥오프 선언만. 실행은 다음 페이지에서 (Shift+T 터미널 오버레이 or 원클릭). "환경은 지금부터 에이전트가 만듭니다."

I am starting the setup process now. Its job is to prepare the laboratory and produce a verification report. While it runs, we can discuss why the laboratory exists.

When I hand this task to an agent, I want more than a statement that the setup succeeded. I want the environment it used, the commands it executed, and a check against the expected outputs. Those details help us distinguish a successful run from a plausible report about a run.

This is already an example of today's main theme. An agent may sound completely certain that the environment is ready. We still need observable evidence: files exist, the relevant code executed, and the verification produced a result we can inspect. The agent's confidence is not our acceptance test.

On the next page I will choose one execution route and start it. If you are following locally, use the same route throughout unless it fails. If your environment needs more preparation, continue following the presentation and return to setup later. Understanding the experiment does not require every laptop to finish at exactly the same moment. We will make the completed reference outputs available as well, and we will identify them as reference values when we use them.

### 05. Three ways to run it — setup & verify

진행 05:26–07:18 · 대본 206단어 · 별도 활동 30초

진행 메모: Setup 실행 페이지. 재학습 버튼 = “seed 고정이라 매번 같은 숫자” 시연용. 에이전트 경로면 T로 터미널 공유.

This page is the execution interface for setup. The manual commands show exactly what the task requires. The prompt describes the same task for an agent, and the buttons call the local server's supported stages. They are different interfaces to the laboratory, so the expected evidence should be comparable.

I will start one route now. Please take a moment to find the route you prefer. If you are viewing the publicly hosted slides, a local execution button may not run anything, because the execution server lives on the presenter's machine. In that case, use your own terminal or follow the demonstration.

There are two checks I want you to notice when setup finishes. First, did training and preparation actually complete? Second, did the resulting outputs pass the supplied verification? A completed process and a passed verification are related, but they are not interchangeable statements.

We also preserve the frozen configuration. If a value differs from the reference, changing the configuration until the number matches would erase the finding. We should inspect the environment and the reported deviation instead. This is a modest example, but the habit scales: establish the acceptance criterion before asking the agent to do the work, then inspect the evidence against that criterion.

[읽지 않음 / 별도 활동] Choose one execution path and start setup; do not wait for completion.

### 06. Detection accuracy is a solved-looking problem

진행 07:18–08:46 · 대본 219단어 · 별도 활동 0초

진행 메모: 숫자 자체는 기존 벤치마크 일반론. "정확도는 이미 높다, 문제는 신뢰다"로 프레임 전환.

Security model evaluations often begin with impressive accuracy numbers. The table gives a broad motivation for why accuracy can make a task look nearly solved. We should not read these illustrative benchmark ranges as a controlled comparison across datasets. A score only becomes interpretable when we know the labels, split, sampling, and evaluation procedure behind it.

Now move from the benchmark to an operational queue. A correct alert may initiate an investigation. An incorrect alert may initiate exactly the same investigation. If we automate the response, that error can also interrupt a legitimate connection or suppress a useful event. A missed attack has a different consequence, which may be more serious in another setting.

This means that the relative cost of an error depends on the action. We should not assume that a false block always costs more than a missed attack, or that the reverse is always true. We need a policy that reflects the environment and the decision being automated.

The next example will make this concrete using simple counts. It asks how many real attacks an analyst sees among all the alerts. That question involves the prevalence of attacks and the false-positive rate, even when the detector's recall looks good. It is a useful bridge from a model score to the work generated by that model.

### 07. The cost of a small false-positive rate

진행 08:46–11:01 · 대본 225단어 · 별도 활동 45초

진행 메모: 가정한 예시. 99,900개의 정상 흐름에 1%를 적용한다. 청중이 정밀도를 먼저 계산하도록 기다린다.

Consider this hypothetical population of one hundred thousand flows. One hundred are attacks, and ninety-nine thousand nine hundred are benign. Suppose the detector catches ninety percent of the attacks and incorrectly flags one percent of the benign flows. These are assumptions for the example, not measurements from our lab.

The detector catches ninety attacks. One percent of the benign population produces nine hundred ninety-nine false alerts. The total alert queue therefore contains one thousand eighty-nine alerts, of which only ninety are true attacks. Before I give the percentage, divide the true attacks by the complete queue.

[읽지 않음: 여기서 45초 활동. Audience calculation: true attacks divided by all alerts.]

The precision is about eight point three percent. That can surprise us if we focus only on ninety percent recall and a one percent false-positive rate. The arithmetic is straightforward. The much larger benign population supplies most of the alerts.

Now imagine that every alert automatically blocks a connection. Compare that with a policy where uncertain alerts enter a review queue and only a validated subset can trigger a limited response. The same detector can create very different operational consequences under those policies.

This example does not tell us which policy to choose. It tells us what to measure before choosing: counts, the traffic mix, and the cost of the resulting action. A threshold that works on a balanced laboratory dataset may behave very differently when attacks are rare.

[읽지 않음 / 별도 활동] Audience calculation: true attacks divided by all alerts.

### 08. Overconfidence — wrong ≠ uncertain

진행 11:01–12:27 · 대본 215단어 · 별도 활동 0초

진행 메모: "모델은 자기가 모른다는 걸 모른다." ECE 언급은 다음 개념 파트에서.

Overconfidence is our first trap. A classifier produces a score through a learned computation. Even when that score lies between zero and one, its format alone does not establish that it accurately represents the chance of being correct.

Think about a training set where one feature separates the classes extremely well. The model can learn to produce very strong scores whenever that feature appears. If the relationship changes, the same computation may still produce a strong score. There does not have to be an exception, a warning, or an obviously malformed output.

The slide uses distance from a learned boundary as an intuition. For a neural model, the confidence comes from its logits and output transformation, rather than a universally meaningful physical distance. The useful point is that the score reflects what the model learned. It does not independently check whether the learned relationship still applies.

This is why I want you to separate two questions. How strongly does the model favor its selected label? And how reliable is that preference on the traffic we currently see? Calibration will help us examine the second question on labeled groups. Our first experiment will show a situation where the strongest-looking answers deserve particular scrutiny. We can only discover that relationship by comparing the score with observed correctness.

### 09. Shortcut learning — the fingerprint trap

진행 12:27–13:53 · 대본 215단어 · 별도 활동 0초

진행 메모: 합성 데이터임을 당당하게 공개 — 메커니즘을 설계했으므로 "왜"까지 설명 가능하다는 게 오히려 강점.

The second trap is shortcut learning. A model can exploit a feature that predicts the label in the training data without capturing the evidence we intended it to use. In network data, a port, fingerprint, or collection artifact may become a convenient separator.

Imagine collecting most attack traffic with one tool and most benign traffic with another. A model might learn the tool's signature. It can then perform well on a test split that preserves the same collection pattern. The evaluation does not reveal what will happen when benign traffic acquires that signature or an attacker avoids it.

Our synthetic lab makes this possibility explicit. We plant a feature whose relationship with the label is strong during training. In part of the test data, we invert and exaggerate that feature while weakening other evidence. This lets us observe how a model reacts when the easy cue points in the wrong direction.

There is a tradeoff in using a designed example. We gain interpretability because the failure mechanism is controlled. We give up any claim that the resulting percentage estimates real-world prevalence. Both facts matter. I will use the lab to explain how a failure can happen, then use a separate traffic experiment to ask whether the proposed reliability signal remains useful under a different challenge.

### 10. Distribution shift — and the label problem

진행 13:53–15:16 · 대본 208단어 · 별도 활동 0초

진행 메모: Part 1 요약. "라벨 없이 계산 가능하고, 모델이 망가질 때 시끄럽게 망가지는 신호" = 오늘의 주제.

The third trap concerns distribution change and the timing of labels. A deployed system may encounter new applications, changing workloads, different infrastructure, or unfamiliar attack behavior. We can observe the traffic and the model outputs immediately. Reliable labels may arrive much later, and sometimes only for a small sample.

So production accuracy is not necessarily unknowable forever. The difficulty is that it may be unavailable at the moment when an automated action must occur. An analyst may confirm an incident tomorrow, while the system must decide whether to act on a connection now.

This timing difference motivates label-free telemetry. We can compute confidence, expert agreement, predicted-class rates, and acceptance rates without knowing the true class. These signals can tell us that something deserves investigation. They cannot, by themselves, prove how much accuracy changed or why it changed.

Keep that distinction throughout the tutorial. A change in a signal is an observation. Calling it an attack, a model failure, or a data-pipeline problem is an interpretation that needs further evidence.

Our objective is to build a workflow that can respond sensibly before complete labels arrive, then use delayed verification to learn whether that response was appropriate. That workflow needs both immediate monitoring and later audits. Neither replaces the other.

### 11. Is the lab ready?

진행 15:16–17:12 · 대본 215단어 · 별도 활동 30초

진행 메모: 에이전트 보고 확인 + 이 표가 자동으로 채워졌는지 확인. 안 채워졌으면 폴백: 터미널 출력 보여주기. 버퍼 여유 있으면 대시보드 빈 화면도 잠깐.

Let us check whether the laboratory is ready. This table is useful because it gives us concrete items to inspect instead of a general success message. We can look at the Python environment, library versions, setup duration, and the dataset identifier.

The content hash is particularly helpful when two people believe they used the same dataset. Matching filenames are weak evidence. Matching content identifiers are much stronger evidence that the inputs agree. The identifier does not establish that the dataset is appropriate for a real deployment, but it helps isolate reproduction problems.

Please compare the report with what appears on screen. If the page is showing the supplied reference rather than a newly generated result, we should say so. The presentation can fall back to reference values, which is useful for teaching, but those values do not prove that a local job just completed.

If setup did not pass verification, the next step is to read the failure and its deviation. We should not spend the session silently changing the specification. We can continue discussing the mechanism using the reference while preserving the failed run for investigation.

With that distinction established, we can move into the dataset design. We now have a shared description of the inputs and an explicit way to compare the outputs.

[읽지 않음 / 별도 활동] Inspect environment and dataset identifiers on screen.

### 12. Meet the dataset (you take it home)

진행 17:12–18:42 · 대본 225단어 · 별도 활동 0초

진행 메모: 데이터 설계 공개. "회피 샘플 = 겉은 요란하게 위장, 진짜 지표는 숨김" 서사 강조.

The synthetic dataset contains six thousand training flows and four thousand test flows. Each flow has thirty features arranged into three groups. Six channels provide attack-related evidence, and one additional feature acts as the planted shortcut.

You can think of the true evidence as several measurements that tend to increase for attack examples. They are imperfect measurements, which is useful because real observations are rarely completely decisive. The shortcut is easier to exploit during training because it has a very strong relationship with the class.

For thirty percent of the test examples, we change the situation. The shortcut becomes misleading and more extreme, while the genuine indicators become less prominent. That combination creates a specific challenge: the easiest cue is persuasive, but points in the wrong direction.

It is important to separate that constructed thirty percent from the measured error rate. Thirty percent is part of the generation design. The model's eventual accuracy depends on how it combines the features and handles the test cases. We should not assume those numbers must be identical.

The advantage of this dataset is that we can ask controlled questions later. What happens if the shortcut becomes stronger? What happens if every expert sees it? Those experiments can test our explanation of the mechanism. They still will not establish how frequently that mechanism occurs in a particular production network.

### 13. Two detectors, one dataset

진행 18:42–20:08 · 대본 215단어 · 별도 활동 0초

진행 메모: "다양성 제약 = 한 shortcut이 판정을 독점 못 하게." 검증 인지형 IDS 아이디어의 미니어처.

We train two detector configurations on this laboratory. The baseline is one small neural network that sees all thirty features. The ensemble contains forty smaller experts, each of which sees a subset of twelve features. Only ten experts are allowed to see the shortcut.

That restriction is the central design choice. If every expert receives the same misleading cue, adding more experts may simply repeat the same error. By restricting access to the shortcut, we try to prevent it from dominating every view of an example.

This also means we are changing more than the score displayed beside a prediction. The model architecture, available evidence, and potentially the predicted label differ between the baseline and ensemble. We will return to that point when interpreting the results.

The configuration pins seeds, splits, and hyperparameters. Reproduction still requires checking the actual output against the expected values and tolerance. We should avoid promising that every environment produces an identical decimal representation without performing that check.

For now, identify what each model emits. The baseline gives a predicted class and confidence. The ensemble gives expert votes, a majority decision, and the fraction supporting that decision. We can compute both scores without labels. To evaluate whether the scores identify errors, however, we will use the labels that the laboratory provides.

### 14. What the experiment compares

진행 20:08–21:35 · 대본 219단어 · 별도 활동 0초

진행 메모: Demo 1과 2는 같은 예측에 점수만 바꾼 비교가 아니다. src/common.py와 experiments/demo2_selective.py를 근거로 비교 범위를 설명한다.

Before looking at results, let us state exactly what the comparison can establish. Both detector configurations use the same generated training and test flows. We hold the dataset and evaluation procedure fixed. That makes their operational results directly comparable on this task.

However, the configurations do not make identical predictions and then attach different uncertainty scores. One uses a single baseline network. The other combines forty feature-subset experts. Their representations and their mistakes can differ.

Suppose the ensemble later accepts many more correct attack alerts than the baseline. A careful conclusion is that the ensemble-and-agreement combination performs better under the particular acceptance criterion in this experiment. We cannot conclude that replacing confidence with agreement, while changing nothing else, caused the entire improvement.

To make that narrower causal claim, we would need a matched comparison. For example, we could hold a set of predictions fixed and compare alternative selection scores, or systematically vary access to the shortcut while controlling the remaining choices. Those would be additional experiments.

This distinction may sound cautious, but it makes the result more useful. It tells another researcher what to reproduce and what remains untested. It also prevents an operator from assuming that a new score can deliver the same benefit without the model diversity that produced it. Keep the complete detector-and-signal combination in view.

### 15. Confidence & calibration

진행 21:35–23:03 · 대본 220단어 · 별도 활동 0초

진행 메모: 수식 없이 개념만. reliability diagram은 말로 설명 ("x축 confidence, y축 실제 정답률, 대각선이 이상적").

Calibration concerns the relationship between stated confidence and observed correctness across predictions. If a collection of predictions all receives confidence near ninety percent, we would like roughly ninety percent of that collection to be correct, under the distribution being evaluated.

This is a group-level statement. It does not identify the ten percent that will be wrong. Even a well-calibrated group contains mistakes, and those mistakes may matter very differently depending on the action attached to them.

A reliability diagram groups predictions by confidence and compares average confidence with empirical accuracy in each group. Expected calibration error summarizes discrepancies across such groups. Those calculations require labels, because correctness is part of the comparison.

For operations, calibration gives us a way to assess whether scores have a reasonable frequency interpretation on representative labeled data. It does not verify an individual alert, and it does not automatically transfer to another traffic distribution.

Imagine a model used to prioritize manual review. Better calibration may help estimate the likely error burden of a batch. Now imagine using the same score to automatically block a critical connection. The aggregate estimate remains useful, but the action may require additional evidence and a much stricter validation procedure. Calibration contributes to that procedure. It is not the whole procedure, which is why we will continue toward selection and verification.

### 16. What miscalibration looks like

진행 23:03–24:32 · 대본 222단어 · 별도 활동 0초

진행 메모: 그림 하나로 ECE 직관 전달. "빨간 간극은 런타임에 안 보인다."

Read this diagram from the horizontal axis to the vertical axis. The horizontal position represents the confidence reported by the model. The vertical position represents the observed fraction of correct predictions in a confidence group. The diagonal is where those quantities match.

The red curve is a schematic illustration of overconfidence. At a point below the diagonal, the model reports greater confidence than the observed accuracy supports. The vertical gap illustrates the mismatch. This is a conceptual picture, not the measured calibration curve of today's experiment.

That distinction matters when we later discuss Demo One. A table of average confidence for correct and incorrect predictions is not itself a reliability diagram. It answers a related question about score behavior, but it does not measure every confidence bin or establish a complete calibration error.

In production, we can observe the horizontal quantity as soon as the model predicts. We need reliable labels to place the corresponding point vertically. Until those labels arrive, the calibration gap is not directly observable for that batch.

When you see an attractive confidence dashboard, ask which of those axes the dashboard actually measures. A smooth stream of high scores only shows that the model keeps producing high scores. It does not show that the points remain close to the diagonal. The next numerical example makes this gap concrete.

### 17. Calibration in one confidence bin

진행 24:32–25:59 · 대본 216단어 · 별도 활동 0초

진행 메모: 예시의 20 percentage points와 20 percent를 구분한다. 이 한 구간의 오차가 전체 ECE는 아니다.

Suppose we have one hundred predictions, each with confidence zero point nine. This is a deliberately simple confidence group. If ninety predictions are correct, the observed accuracy is ninety percent and agrees with the stated confidence in this group.

If only seventy are correct, the average confidence still says ninety percent, but the observed accuracy is seventy percent. The discrepancy is twenty percentage points. I use percentage points because we are subtracting two percentages. We are not claiming a twenty percent relative change.

Now consider what the first case actually tells an analyst. There are still ten incorrect predictions. The group-level match does not identify them. An individual example could be one of the ten even though it belongs to a well-calibrated group.

Also, this single bin does not determine calibration for the entire model. Other confidence groups could behave differently, and different traffic subgroups could be hidden inside the same average. The number of labeled examples affects how precisely we can assess the match.

This is why I would report both the calibration summary and the evaluation context: which data, which period, how many examples, and which grouping procedure. If we cannot answer those questions, a claim that the model is calibrated is incomplete. We need enough context to know what population that statement describes.

### 18. Can we fix calibration? — mostly, yes

진행 25:59–27:29 · 대본 225단어 · 별도 활동 0초

진행 메모: "온도 하나 맞추는 건 공짜다 — 안 할 이유가 없다." 단, 다음 장에서 함정.

There are established ways to improve calibration on a suitable labeled validation set. Temperature scaling adjusts the model's logits using a learned scalar. Platt scaling fits a logistic transformation to scores. Isotonic regression fits a monotone mapping. The table gives a short orientation rather than a universal ranking.

The important workflow is to fit the calibration step using representative validation data and assess it on data that did not choose the transformation. A flexible mapping can fit the validation observations without giving us the same behavior on future traffic.

Temperature scaling is attractive because the fitted transformation is simple. The work by Guo and colleagues provides a useful starting point for this topic. Its results motivate evaluation of the method, rather than a promise that every network-security deployment will benefit equally.

There is also a conceptual limit. Adjusting a score does not necessarily change which label the model selects, and it does not supply missing packet evidence. If the model learned a misleading relationship, a better frequency interpretation on familiar validation data does not remove that relationship.

So I would treat calibration as one part of a measured deployment process. Fit it, evaluate it, and record the data used. Then ask whether the incoming traffic still resembles the population on which the calibration statement was established. That last question takes us to the next slide.

### 19. The catch: calibration is a snapshot

진행 27:29–28:55 · 대본 217단어 · 별도 활동 0초

진행 메모: "어제의 분포에 맞춘 스냅샷" — demo 3 복선. 캘리브레이션만 믿으면 안 되는 이유.

A calibration result belongs to an evaluation setting. The model, score transformation, and validation population together support the claim. When the population changes, the old relationship between confidence and correctness may no longer hold.

Imagine that most high-confidence validation predictions came from familiar applications. Later, a new application generates similar surface features with a different meaning. The model can keep assigning high confidence while its correctness changes. A stable average score would not reveal the calibration failure by itself.

We should avoid assuming a universal order in which metrics degrade. Calibration does not always fail first, and accuracy does not always change by the same amount. The point is that high or stable confidence is insufficient evidence that yesterday's calibration remains valid.

Recalibration also needs labeled examples. Those examples may arrive through delayed incident review or deliberate sampling. If they come only from the most suspicious alerts, they may not represent the complete production population. The sampling process is therefore part of the evaluation.

For an operational system, I would record when calibration was assessed, the traffic covered, and the conditions that trigger a new assessment. We can watch label-free changes while waiting for labels, but we should describe them as monitoring signals. We cannot claim that monitoring an average confidence score has directly measured current calibration.

### 20. So… is confidence an error signal at all?

진행 28:55–30:19 · 대본 208단어 · 별도 활동 0초

진행 메모: 킥오프 ② 의식. "개념 설명 후 결과를 확인합니다. 그동안 uncertainty 이야기."

We now have enough background to state the first experimental question precisely. On our synthetic test data, does confidence decrease when the baseline is wrong? The initial table suggested the opposite. We will reproduce that observation and compare it with the ensemble's agreement behavior.

The experiment groups predictions using known labels, then averages the relevant score within correct and incorrect groups. That means it is an offline diagnostic. In deployment, without the labels, we would not know which group contains a new prediction.

Nevertheless, this diagnostic can tell us whether a candidate selection signal points in a useful direction on the evaluation. If mistakes systematically receive stronger scores, simply trusting the largest score deserves scrutiny. If mistakes receive weaker scores, we have a reason to examine the full distribution and potential thresholds.

I will start the experiment on the next page. While it runs, we will introduce the uncertainty language needed to interpret the ensemble. When we return to the result, please look for the direction and size of the differences before drawing a deployment conclusion.

We are testing a concrete claim with a specified dataset and configuration. If the verification does not match, we will report the difference rather than alter the question after seeing the answer.

### 21. Three ways to run it — pick yours

진행 30:19–31:56 · 대본 207단어 · 별도 활동 15초

진행 메모: 실행 페이지 견본. 버튼이면 오른쪽 화면에 출력이 흐르고, 에이전트면 T 오버레이로 터미널 공유. 어느 쪽이든 결과는 다음 체크포인트 표에 자동 반영.

This is the execution page for Demo One. I will launch the experiment once and confirm that it starts. If you are using an agent, the prompt should lead it to run the relevant command and verify the output. If you are using the terminal, you can inspect those same steps directly.

Notice that our question is already specified before the result appears. We want the means for correct and incorrect predictions, and we want to compare the reproduced values with the pinned reference. A generic statement that the model performed well would not answer that question.

When the output arrives, we will distinguish the baseline's confidence from the ensemble's agreement. Each is evaluated relative to its own prediction correctness. This is another reason not to treat the result as a score-only substitution on identical decisions.

If the process fails, the output is still useful evidence about execution. It is not evidence that the scientific hypothesis is false. We first need to distinguish a pipeline failure from a completed experiment whose measured values disagree with the reference.

I am leaving the computation running as we move on. The next concepts explain why several experts can sometimes reveal a problem that remains hidden inside a single confident output.

[읽지 않음 / 별도 활동] Launch Demo 1 once and confirm that the job starts.

### 22. Uncertainty — what kind of "don't know"?

진행 31:56–33:21 · 대본 212단어 · 별도 활동 0초

진행 메모: "모델 하나는 자신의 무지를 못 본다" → 다음 슬라이드에서 앙상블로 연결.

Uncertainty is often divided into aleatoric and epistemic components. The words are less important than the distinction they help us make. One concerns ambiguity remaining in the observations. The other concerns limitations in what the model has learned.

For the first case, imagine two flows with the same measured features but different true meanings. Perhaps the features omit context that would distinguish them. Given the available representation, the classifier cannot reliably separate the cases simply by becoming more confident. Better measurements could change that situation, so irreducibility is relative to what we observe.

For the second case, imagine a pattern that is poorly represented in training. Different plausible models may interpret it differently because the data did not constrain their behavior well. More relevant examples or a better representation could reduce that uncertainty.

These categories are helpful, but an operational change need not fit perfectly into one box. Evasion, new applications, and measurement changes can interact. A single score does not reliably diagnose the cause.

The ensemble idea is to inspect variation across learned views. If the views disagree, that can tell us the decision deserves further investigation. If they agree, we still need to ask whether they share the same blind spot. Our second laboratory will make that limitation especially important.

### 23. Estimating uncertainty, in practice

진행 33:21–34:52 · 대본 227단어 · 별도 활동 0초

진행 메모: "다양성이 기교를 이긴다." 우리 랩의 subset expert는 deep ensemble의 경량 변형.

There are several practical approaches to estimating uncertainty. This table helps locate our method among them. Monte Carlo dropout repeats inference with stochastic dropout. Deep ensembles combine independently trained models. Other approaches produce richer output distributions in a single pass. Our laboratory uses experts that see different feature subsets.

Each choice has a cost model. Repeated forward passes consume computation. Multiple models require training and storage. A single-pass approach can reduce inference cost while introducing other modeling and validation demands. The appropriate choice depends on the deployment constraints and the evidence produced by evaluation.

For this tutorial, feature subsets make the diversity mechanism easy to inspect. We can identify which experts are exposed to the planted shortcut. That is more informative for our controlled question than simply saying we trained many models.

However, different inputs do not guarantee independent errors. Experts may share training labels, preprocessing, model families, and enough common evidence to fail together. A deployment should assess the behavior of the resulting combination rather than infer reliability from the model count.

When someone proposes an ensemble, I would ask what creates the diversity and what experiment demonstrates its value. Forty copies of one mistake do not give forty independent confirmations. Our next slide defines exactly how the laboratory summarizes the votes, so we can interpret the number without giving it more meaning than it has.

### 24. A practical proxy: ensemble agreement

진행 34:52–36:20 · 대본 219단어 · 별도 활동 0초

진행 메모: VALIDS는 사례 1장으로만. 우리 랩 구성(40 expert, shortcut 노출 10개 제한 = 다양성 제약) 설명.

Agreement in this laboratory is the fraction of experts supporting the majority decision. With forty binary predictions, we count how many vote for each class and take the larger fraction. It is a descriptive statistic of the votes.

That makes it available without labels. We do not need to know whether the majority is correct to count its support. This availability is useful for runtime monitoring and selection, but it also explains why agreement is not automatically a probability of correctness.

Our feature-subset design tries to give experts different evidence. Restricting shortcut access means some experts must reach a decision using other features. When the shortcut conflicts with those features, their disagreement may expose the conflict.

Verification-aware detector designs develop this idea further by making evidence and related checks part of the output. We will discuss the operational meaning of evidence checks later, without going into a particular architecture in depth.

For now, resist turning the intuition into a universal rule. Unfamiliar traffic does not have to produce disagreement. If all the experts extrapolate in the same direction, agreement can stay high. Conversely, disagreement does not prove an attack. It can indicate ambiguity, a benign novelty, or a modeling problem. We need to evaluate the signal and connect it to a response appropriate for the uncertainty it actually reveals.

### 25. Agreement counts votes

진행 36:20–37:50 · 대본 226단어 · 별도 활동 0초

진행 메모: 가상의 투표 예시. 0.8을 정답확률 80%로 읽지 않는다. 동률 처리 규칙과 합의도 크기는 별개다.

Let us calculate agreement directly. In the first row, thirty-two experts vote attack and eight vote benign. The majority has thirty-two of forty votes, so agreement is zero point eight. That number says eighty percent of the experts backed the chosen class. It does not say the prediction has an eighty percent chance of being correct.

In the second row, the votes split evenly. Agreement is zero point five. The implementation needs a rule for which label wins a tie, but that rule does not make the split less ambiguous.

The third row is the important counterexample. All forty experts share the same mistaken prediction. Agreement is one, even though the decision is wrong. We can construct that situation if the experts rely on the same misleading evidence or respond similarly to an unfamiliar pattern.

Ask what additional information would help distinguish unanimous expertise from a shared blind spot. We might inspect which features the experts used, compare evidence against raw records, examine a changed traffic slice, or audit a sample with labels.

This question prepares us for the contrast between the labs. In the synthetic experiment, restricted shortcut access may make disagreement informative. In the later traffic experiment, high agreement may persist through a serious failure. The lesson is to test diversity under the conditions that matter, rather than treat unanimity as its own validation.

### 26. The label-free signal menu

진행 37:50–39:20 · 대본 224단어 · 별도 활동 0초

진행 메모: 레퍼런스 슬라이드 — 사진 찍는 청중 많을 장. 잠시 머물기.

Here is a menu of signals that can be computed without immediate labels. Confidence is inexpensive once the model has produced its output. Agreement uses the expert votes. Margin and entropy summarize properties of an output distribution. Evidence perturbation checks how the decision responds when selected information changes. Trends track these quantities across time.

The table's short descriptions are possible uses, not guarantees that each signal detects a particular failure. An unfamiliar input may remain confident and unanimous. A perturbation can change a decision because the modified input is unrealistic. A rate can move because the workload changed legitimately.

The operational value comes from testing what each signal does in a relevant evaluation and recording what it leaves ambiguous. If two signals are based on nearly identical information, combining them may add less independent evidence than we expect.

Consider an alert with high confidence and low agreement. That disagreement between summaries gives us a reason to inspect the evidence. Now consider high confidence and high agreement while the accepted-alert rate suddenly changes. The individual scores look reassuring, but the aggregate behavior deserves attention.

We will see versions of both patterns today. The point of the menu is to give us several observations with different failure modes. Later, delayed labels help determine whether those observations predicted actual errors and whether the response policy was useful.

### 27. Conformal prediction — guarantees, with fine print

진행 39:20–40:53 · 대본 234단어 · 별도 활동 0초

진행 메모: 요즘 가장 뜨거운 도구 — 그러나 drift가 전제를 깬다는 것까지 말해야 정직한 소개.

Conformal prediction offers another way to express uncertainty. A standard classification construction returns a set of possible labels. Depending on the example and calibration procedure, that set can contain one label, several labels, or sometimes no label.

Under the required assumptions, the procedure provides a marginal coverage guarantee at a chosen level. For example, a ninety-five percent target concerns how often the set contains the true label across the relevant population and randomness. It does not mean that every individual singleton prediction has a ninety-five percent probability of being correct.

For binary security classification, a set containing both benign and attack leaves the decision unresolved. A singleton may be more actionable, but action still depends on validation and cost. An empty set also needs an explicit handling rule. A system should not silently convert every output into a confident single-class action.

The introductory reference by Angelopoulos and Bates explains these constructions and their assumptions in more detail. For our discussion, the crucial issue is exchangeability between the relevant calibration and test observations. Arbitrary distribution shift can invalidate the usual guarantee.

Monitoring set sizes can reveal changes in behavior, but stable set sizes do not prove that coverage remains valid. We still need suitable labels to audit coverage. This repeats the distinction we made for calibration: a runtime observable is valuable, but it is not a replacement for the labeled property we ultimately care about.

### 28. Before the result lands…

진행 40:53–43:01 · 대본 208단어 · 별도 활동 45초

진행 메모: 청중 투표 45초. 활동 표식에서 멈추고 투표를 받은 뒤 대본을 이어 읽는다.

Before we reveal Demo One, I want your prediction. On the synthetic test set, which group has the higher average baseline confidence: the correct predictions, the wrong predictions, or approximately the same level?

Please commit to an answer before looking at the result. If you choose the correct group, your intuition may be that strong scores reflect strong evidence. If you choose the wrong group, your explanation might involve the exaggerated shortcut in the evasive examples. If you choose equal, perhaps you expect the model to remain strongly confident almost everywhere.

The value of this exercise is the reason behind the vote. We already saw a reference number at the beginning, but I want you to connect that number to the mechanism. A remembered answer is less useful than a prediction you can justify from the dataset design.

[읽지 않음: 여기서 45초 활동. Collect the audience vote before showing the result.]

After the vote, we will inspect the actual output and its verification. Then we will compare agreement using the same style of summary. Please remember that each detector defines its own correct and incorrect groups.

Finally, think ahead to the operational question. Even if we predict the direction of the means correctly, we still do not know how many alerts a threshold can safely retain. That requires the next experiment.

[읽지 않음 / 별도 활동] Collect the audience vote before showing the result.

### 29. Demo 1 — confidence vs agreement

진행 43:01–44:59 · 대본 218단어 · 별도 활동 30초

진행 메모: 에이전트 보고 낭독 + 이 표(자동 채움)와 대조. 훅 슬라이드의 0.9457/0.9635가 여기서 재현됨을 명시. → 킥오프 ③.

Here is the result. First, check whether these are completed local outputs or the clearly identified reference values. The pinned reference shows baseline confidence around zero point nine four six on correct predictions and zero point nine six four on wrong predictions. The difference has the troubling direction we anticipated.

Now look at ensemble agreement. Its mean is about zero point eight eight seven on correct predictions and zero point eight two four on wrong predictions. In this evaluation, agreement decreases among the ensemble's errors. That direction is more promising for a selection signal.

We should inspect the verification report before accepting that the local run reproduced the result. A populated slide alone is not enough, because the page can display reference values when live output is unavailable.

Next, look at the chart. The summary is useful, but it compresses many examples. A gap between averages does not tell us whether individual score distributions overlap substantially. Nor does it tell us which threshold would give a useful acceptance rate.

The experiment therefore supports a focused conclusion: these detector-and-signal combinations behave differently on their errors in the controlled setting. Agreement points in a useful direction here. To learn whether that difference supports selective automation, we need to define what counts as an accepted alert and measure the resulting counts.

[읽지 않음 / 별도 활동] Read the populated table and point to the chart.

### 30. What Demo 1 establishes

진행 44:59–46:27 · 대본 222단어 · 별도 활동 0초

진행 메모: 각 모델의 정오답 집단이 다를 수 있음을 다시 짚는다. 이 장에서는 결과를 해석하고 다음 데모의 질문을 도출한다.

Let us pause to separate the result from the claims we might be tempted to add. We observed that the baseline's incorrect predictions had higher average confidence. We also observed that the ensemble's incorrect predictions had lower average agreement. Those statements are supported by the measured groups.

We have not shown that every high-confidence prediction is wrong, or that every low-agreement prediction is an attack. We have not shown that agreement always catches unfamiliar traffic. We also have not isolated a score-only causal effect, because the two detector configurations can make different predictions.

One useful next step is to examine a threshold. Suppose we accept only attack predictions whose score exceeds a chosen cutoff. We can then count true accepted attacks, false accepted alerts, and how many test flows are covered by the accepted subset.

That translates a distributional observation into a policy question. The score is useful only to the extent that it helps us make a decision with acceptable consequences. A signal can separate the means and still leave too much overlap for the desired policy.

Demo Two will use a deliberately strict descriptive criterion: no false accepted attack alerts in the evaluated sample. We will see how much each configuration retains, then discuss why a threshold chosen with that sample should not be treated as a guaranteed production rule.

### 31. Demo 2 — can we trust some alerts completely?

진행 46:27–47:59 · 대본 229단어 · 별도 활동 0초

진행 메모: 킥오프 ③ 선언. 실행은 다음 페이지. "그동안 selective prediction 개념."

Demo Two asks whether we can identify a subset of attack predictions with very high observed precision. We will compare the baseline's confidence gate with the ensemble's agreement gate. The goal is to understand selective acceptance, rather than force every prediction into an automated action.

The descriptive target in this demonstration is precision one point zero on the evaluated sample. That means there are no false positives among the accepted attack alerts in that sample. It does not mean there are no missed attacks, and it does not guarantee that future accepted alerts will all be correct.

This is a useful thought experiment because a detector may be much more useful on a limited subset than its overall accuracy suggests. At the same time, a trivial gate that accepts almost nothing can look extremely precise. We therefore need to report how much it retains.

I will launch the experiment next. While it runs, we will define the metrics carefully, including the denominators. When the result arrives, I want you to ask both how reliable the accepted sample appears and how many actual attacks it contains.

There is one evaluation detail we will revisit after the result: the demonstration searches thresholds using the labeled test sample itself. That makes the result an illustration of what is achievable within that sample, rather than an independent estimate of a preselected production threshold.

### 32. Three ways to run it — precision-1.0 gate

진행 47:59–49:39 · 대본 213단어 · 별도 활동 15초

진행 메모: Demo 2 실행 페이지. 결과는 다음 체크포인트 표에 자동 반영.

I am starting Demo Two using the same execution pattern. Choose one route, launch the command, and inspect its report when it finishes. The lab is already trained, so this stage evaluates the available model outputs and searches candidate thresholds.

Before we leave the page, notice the desired output. We need the chosen threshold, coverage, and the number of true accepted attacks. These are concrete quantities we can compare with the pinned reference. A statement such as the ensemble is more trustworthy would be too broad to verify.

If you use an agent, it should report what the script measured and how verification went. It should not change the target, loosen a tolerance, or rewrite the configuration to make the run look successful. The request and the check define the task.

The execution time can overlap with our explanation of selective prediction. We do not gain insight from waiting on this page after the process starts. If the local environment is slow, we can inspect the reference result and later compare the completed run, while clearly distinguishing the two.

Let us now define what it means to accept a prediction. That definition is where a model output becomes an operational policy, and small ambiguities there can produce large misunderstandings in the reported metrics.

[읽지 않음 / 별도 활동] Launch Demo 2 once.

### 33. Selective prediction & abstention

진행 49:39–51:06 · 대본 217단어 · 별도 활동 0초

진행 메모: abstention 경로가 있어야 selective prediction이 의미 있음 → Part 4 운영 트리 예고.

Selective prediction allows a system to abstain on some inputs. Instead of treating every model output as equally actionable, we use a rule to choose the subset on which the system is allowed to proceed.

In this demonstration, acceptance has a specific meaning. The model must predict attack, and its selection score must pass the threshold. A benign prediction does not enter the accepted attack-alert set, even if the model is very confident about it.

Raising a threshold often changes the balance between the reliability of retained predictions and the amount of work the system can handle automatically. We should measure that behavior rather than assume every metric improves monotonically. The observations in a finite sample can be irregular.

Most importantly, abstention needs a destination. If rejected alerts disappear, the gate may simply hide difficult cases. An operational design might route them to review, collect additional evidence, or use a separate conservative procedure. The choice depends on the action and its consequences.

A selective system can therefore be evaluated at two levels. How well does the acceptance rule perform on the retained subset? And what happens to everything outside that subset? The first is a model-and-policy measurement. The second is a workflow responsibility. The next slide gives the exact metric definitions we need for the first question.

### 34. Precision, coverage, and recall

진행 51:06–53:34 · 대본 219단어 · 별도 활동 60초

진행 메모: coverage는 공격 중 검출 비율이 아니다. 이 구현에서 acceptance는 공격 예측만 포함한다.

These three metrics use different denominators, so let us read them carefully. Precision divides true accepted attacks by all accepted attack alerts. It asks how many of the alerts allowed through the gate are actually attacks.

Coverage in this implementation divides all accepted attack alerts by all four thousand test flows. It asks what fraction of the complete test population enters the accepted attack-alert set. Other selective prediction settings may define coverage over all retained predictions, so the implementation-specific definition matters.

Recall divides true accepted attacks by all one thousand nine hundred fifty-nine actual attacks. It asks how many attacks survive both the detector and the gate. An attack rejected by the gate does not contribute to this accepted-set recall.

Take a moment to identify the denominator for each metric without looking at the table. This simple habit prevents many mistakes when comparing selective systems.

[읽지 않음: 여기서 60초 활동. Participants identify the three denominators.]

In the reference result, the agreement configuration retains one thousand two hundred eighty-seven true attacks with no false accepted alerts in the selected sample. Its coverage is about thirty-two point two percent of all test flows, while its recall is about sixty-five point seven percent of actual attacks. Those are different descriptions of the same retained count. Neither says that all remaining flows are benign or that the complete operational workflow has resolved them.

[읽지 않음 / 별도 활동] Participants identify the three denominators.

### 35. Why precision 1.0 matters in a SOC

진행 53:34–55:02 · 대본 221단어 · 별도 활동 0초

진행 메모: [버퍼 슬라이드] 시간이 밀리면 통째로 스킵 가능. 체크포인트 ③이 아직이면 여기서 시간 벌기.

Why use such a strict precision target in a security tutorial? Some automated actions can have substantial consequences, so a team may want strong evidence before allowing a model to initiate them. A descriptive zero-false-positive gate makes the tradeoff easy to see in a small laboratory.

But observed precision one point zero should not become a slogan for safe automation. It depends on the sample, the threshold-selection procedure, and the population. A small accepted set with no observed errors leaves substantial uncertainty about future behavior.

Consider two systems. One accepts a handful of obvious attacks. Another accepts a much larger number with the same observed precision. Their value to an analyst can differ greatly, which is why retained counts and recall belong beside precision.

Now consider the cases neither system accepts. Someone still owns those decisions. A queue can become unmanageable if the gate routes too much work to analysts. A policy therefore needs a capacity assumption as well as a quality target.

I would begin with the action being considered, establish an acceptable error burden and review process, and evaluate a frozen policy on representative later data. Our lab's strict target gives us a clear comparison, but the production target must come from that operational analysis. It should not come from copying the most impressive number on a tutorial slide.

### 36. Demo 2 — the trusted zone, measured

진행 55:02–56:59 · 대본 217단어 · 별도 활동 30초

진행 메모: "같은 데이터에서 서로 다른 detector-and-signal 조합을 비교한 결과, 약 17배." → 킥오프 ④로.

The reference results show a large difference in retained attacks. The baseline confidence gate uses a threshold around zero point nine eight eight four. It retains seventy-six true attacks, covering one point nine percent of the four thousand test flows.

The ensemble agreement gate uses a threshold of zero point seven seven five. It retains one thousand two hundred eighty-seven true attacks, with coverage about thirty-two point two percent. Both selected samples have no false accepted attack alerts under the demonstration's threshold search.

Dividing the retained attack counts gives a ratio of about sixteen point nine three. That is the source of the roughly seventeen-times statement. The ratio concerns accepted true attacks under this particular criterion. It is not a seventeen-times improvement in overall accuracy or a guaranteed improvement in a deployment.

Also remember our comparison protocol. The baseline and ensemble are different detector configurations. The result supports the ensemble-and-agreement combination in this controlled setting, without isolating how much of the gain comes from predictions, evidence diversity, or the selection score.

Please inspect the chart and the printed verification together. If the local values differ, report the actual values and deviation. Then we must address the question that matters before transferring the threshold: which examples were allowed to choose it? The next slide makes that limitation explicit.

[읽지 않음 / 별도 활동] Inspect threshold, coverage, and true-positive counts.

### 37. A threshold needs an untouched test

진행 56:59–58:58 · 대본 223단어 · 별도 활동 30초

진행 메모: experiments/demo2_selective.py에서 y_te로 threshold를 탐색한다. 실험 코드는 변경하지 않고 일반화 평가와 구분한다.

In Demo Two, the script searches thresholds using the labeled test data and selects a threshold that meets the precision target while retaining the largest coverage. It then reports performance on that same sample. This is a descriptive exploration of the sample, not an independent evaluation of a threshold fixed beforehand.

A deployment study needs a clearer separation of roles. Training data fits the detector and preprocessing. Validation data selects the threshold and other policy choices. An untouched test, preferably reflecting the intended deployment setting, estimates the behavior of that frozen policy.

Please identify the selection step in the lab procedure. Once a label has influenced the threshold, the resulting performance on that example is no longer an untouched test of the policy. Renaming the data does not change its role.

There is another limit even with a clean separation. Zero observed false positives is finite evidence. It does not prove the true future false-positive probability is zero. We should report the accepted sample size and uncertainty appropriate to the evaluation, then continue monitoring after deployment.

We are preserving the demonstration as it is because it answers a useful illustrative question. The correct response is to state its scope and design a separate validation study for operational use. Changing the experiment silently would make its reference numbers and teaching purpose harder to interpret.

[읽지 않음 / 별도 활동] Participants identify which split chooses the threshold.

### 38. Lab 2 — the dataset you all know

진행 58:58–60:25 · 대본 217단어 · 별도 활동 0초

진행 메모: "다들 아는 그 데이터셋." 결함 공개가 오히려 주제와 부합. 화수 학습→목금 평가 구조 설명. 파이프라인 실행은 다음 페이지.

We now move to a different laboratory using CIC-IDS2017 traffic. The synthetic example gave us a mechanism we controlled. This experiment asks how a fixed detector behaves across traffic slices from different days.

For the drift track, training uses Tuesday and Wednesday flows. A separate holdout from those days supports threshold selection. Thursday and Friday then provide later evaluation slices, with different traffic and attack composition. The slide summarizes the roles rather than presenting a universal chronology of network behavior.

The models still include a baseline and forty feature-subset experts, but the feature space and fitted models belong to this traffic dataset. We should not transfer the synthetic threshold to this lab or compare the raw percentages as if the two populations were interchangeable.

The dataset also represents a particular collection setting. Its age, construction, and sampling limit claims about a current production network. For today's purpose, the useful question is narrower: can individual score summaries remain reassuring while measured performance changes substantially across these slices?

That question challenges an easy reading of the first lab. If agreement worked on the planted shortcut, it may be tempting to trust it everywhere. The second lab tests whether that confidence in agreement survives a different evaluation. Before running it, we will make the time split and threshold-selection procedure explicit.

### 39. The time split is part of the experiment

진행 60:25–61:52 · 대본 217단어 · 별도 활동 0초

진행 메모: src/config_cic.py와 experiments/demo3_cic_drift.py 기준. holdout은 임계값 선택에 사용되어 완전히 독립인 최종 테스트가 아니다.

Here is the protocol for Demo Three. We fit the models using the training portion of Tuesday and Wednesday. We then use a separate holdout from those days to choose a confidence threshold. The threshold selects attack predictions under the same strict descriptive precision target.

After that selection, the models and threshold stay fixed while we evaluate Thursday and Friday. This preserves the temporal challenge: later data must not influence the fitted detector or the threshold before we measure its behavior.

Notice that the holdout has a selection role. Its accepted-set precision is not an untouched estimate of a policy chosen elsewhere. The later slices give us the more relevant check of whether that selected rule transfers.

Also notice what the time split does not isolate. Several things can change between days: class proportions, attack families, feature distributions, and collection-related properties. A performance difference across days does not identify which one caused it.

That causal uncertainty affects the operational response. If a rate changes, we investigate the pipeline and the traffic as well as the model. We should not label every temporal difference adversarial evasion. The experiment can show a failure of transfer without proving a single explanation for the failure. That is enough to motivate monitoring and an explicit process for deciding when to restrict automation.

### 40. Dataset → models, live — download · preprocess · train

진행 61:52–63:48 · 대본 216단어 · 별도 활동 30초

진행 메모: CIC 파이프라인 실행 페이지. 발표 시 Preprocess/Train은 사전 완료 상태 — 시간 여유에 따라 라이브 재실행 여부 결정.

This page shows the preparation pipeline for the traffic lab. Downloading, preprocessing, and training are separate steps, and the distinction helps us understand both reproduction and timing. The planned session assumes these expensive preparation steps are already complete on the presenter machine.

I will inspect the prepared artifacts and the available execution state. We can show how to rerun the pipeline without spending the presentation waiting for a download. If you are setting up for the first time, you can follow the commands later using the supplied repository.

The verification principle remains the same. A model file existing on disk does not, by itself, identify the training data or prove that the intended split was used. We want the preparation procedure, configuration, and resulting checks to agree.

For the upcoming experiment, the most important requirement is that the drift-track models were fitted on the earlier training data. If we accidentally use a model trained with later data, we change the question even if the command produces a plausible table.

Once the prepared artifacts are confirmed, we only need to run the evaluation stage. That lets us spend our time on interpreting the output. In a tutorial, preparation should support the discussion rather than make the audience wait through work that teaches little about the reliability question.

[읽지 않음 / 별도 활동] Inspect prepared CIC artifacts; use cached preparation for this schedule.

### 41. Demo 3 — then the week goes on

진행 63:48–65:13 · 대본 213단어 · 별도 활동 0초

진행 메모: 킥오프 ④ 선언. 실행은 다음 페이지. "그동안 explainability 이야기."

We are ready to start Demo Three. The hypothesis is deliberately different from Demo One. This time, average confidence and average agreement may remain high while baseline accuracy on a later slice falls. We will also inspect how often the baseline predicts attack and how often its attack predictions pass the frozen confidence gate.

Please distinguish the two kinds of information in the final table. Accuracy needs labels and is available to us because this is a labeled experiment. Confidence, agreement, predicted-attack rate, and accepted-attack rate can be computed as traffic arrives.

In an operational setting, we might see the score and rate rows first. The accuracy row could become available only after a delayed audit. Our challenge is to decide what those immediately observable rows justify doing before we know the answer.

We will start the evaluation on the next page and use the running time to discuss explanations, evidence tests, and monitoring. Those concepts matter because a changed rate alone does not diagnose the failure.

When we return, avoid looking only for a lower agreement value. That would assume the conclusion from Lab One transfers unchanged. Read every row, consider what is observable without labels, and ask which additional evidence would help distinguish a model problem from a legitimate traffic change.

### 42. Three ways to run it — the week goes on

진행 65:13–66:51 · 대본 207단어 · 별도 활동 15초

진행 메모: Demo 3 실행 페이지. 결과는 다음 체크포인트 표에 자동 반영.

I will launch the drift evaluation now. It loads the prepared traffic data and models, applies the fixed procedure to each slice, and writes a verification report. As before, one execution route is enough.

The command should evaluate the drift track. That detail matters because a repository can contain several models and several experimental splits. A successful run of the wrong experiment would not answer the question we just stated.

When the report arrives, we will inspect the holdout, Thursday, and Friday results. The presentation highlights holdout and Friday to make the contrast readable, while the complete output gives additional context. We should keep the intermediate slice available rather than pretend the comparison is a continuous measurement of every moment in the week.

If a local run cannot complete, we can discuss the supplied reference with that status made explicit. The values remain useful for understanding the experiment, but they should not be described as newly reproduced on this machine.

I am moving on while the evaluation runs. The next question is what kind of explanation would actually help an analyst investigate a suspicious output. A fluent description of the decision may sound convincing. We need to ask what observations or interventions would let us check it.

[읽지 않음 / 별도 활동] Launch Demo 3 once.

### 43. Explainability — necessary, not sufficient

진행 66:51–68:20 · 대본 223단어 · 별도 활동 0초

진행 메모: 설명 가능 ≠ 검증 가능. 다음 장에서 최소 증거 집합으로 구체화.

Explainability can help us understand which inputs influence a model's decision. An attribution method might highlight a feature, a sequence of bytes, or a region of a representation. That can be useful for directing attention, especially when the original input is large.

But an explanation is not automatically evidence that the selected label is correct. A model can consistently use the wrong cue, and an explanation can faithfully describe that reliance. In that case, the explanation reveals the problem only if someone checks what the cue means.

Imagine an alert described as suspicious because of a rare fingerprint. The description sounds reasonable. We still need to ask whether the fingerprint was measured correctly, whether it is actually unusual in this environment, and whether the surrounding behavior supports the attack interpretation.

A testable claim gives the analyst a more concrete next step. We can ask whether the prediction persists when only the cited evidence remains, or whether removing that evidence changes the result. These tests describe model behavior under a chosen intervention. They do not automatically establish the real-world cause of the event.

The practical objective is to make the explanation useful for investigation. It should point to inspectable records and checks whose outcomes could change our decision. An explanation that cannot be challenged may be persuasive without helping us determine whether to act.

### 44. Evidence-based verification

진행 68:20–69:48 · 대본 219단어 · 별도 활동 0초

진행 메모: VALIDS 충분성/필요성 개념을 일반화해 소개. 깊이는 여기까지 (아키텍처 상세 금지).

Evidence-based verification asks what information actually supports the prediction under an explicit test. Two useful concepts are sufficiency and necessity. Sufficiency asks whether the selected evidence alone can preserve the decision. Necessity asks whether removing it changes the decision.

Those questions depend on how we keep or remove evidence. Replacing a feature with zero, for example, may create an unrealistic input. A changed prediction could reflect that artifact rather than a meaningful dependence on the real-world signal. We must define the intervention and interpret it carefully.

There is also a distinction between finding a small sufficient set and proving that it is the smallest possible set. In a practical system, a procedure may identify a compact candidate without establishing global minimality. The report should describe what the procedure actually tested.

For operations, the important benefit is a narrower investigation target. If the decision depends strongly on a timing channel, the analyst can inspect the underlying timestamps and extraction logic. If several experts cite the same questionable feature, apparent model diversity may be less convincing.

We are not implementing these evidence tests in today's three demos. They are a design direction for making future outputs more auditable. The next slide is a hypothetical example that illustrates the workflow and its limitations, rather than an additional measured result from the repository.

### 45. Evidence, in action — one flow, audited

진행 69:48–71:46 · 대본 220단어 · 별도 활동 30초

진행 메모: 가상 사례. 활동 표식에서 30초간 raw evidence 확인 방법을 생각하게 한 뒤 예시 답을 설명한다.

Consider a hypothetical alert labeled as command-and-control traffic. The model cites regular timing, a rare TLS fingerprint, and fixed-size uplink bursts. These observations give the analyst concrete places to look, but they do not yet establish that the flow is malicious.

Suppose a defined sufficiency test retains those measurements and the model still predicts command and control. Then a defined removal test changes the timing evidence, and the model switches its decision. We have learned that the prediction is sensitive to timing under those interventions.

What raw evidence would you inspect next? Take a moment to choose a check. [읽지 않음: 여기서 30초 활동. Audience proposes a raw-evidence check for the hypothetical flow.]

One possibility is to examine packet timestamps and confirm that the regularity exists before aggregation. Another is to ask whether a legitimate periodic service produces the same pattern. We could also inspect whether clock handling or preprocessing created the regularity.

The key is that the check can change our interpretation. If the timing signal is a processing artifact, the explanatory story loses support. If it is real, we still need context to decide whether it indicates a threat.

This example separates model dependence from incident truth. The perturbation helps us locate what matters to the model. The raw-record investigation helps us determine whether that evidence supports the operational claim. Both are useful, and neither should be silently substituted for the other.

[읽지 않음 / 별도 활동] Audience proposes a raw-evidence check for the hypothetical flow.

### 46. Where drift actually comes from

진행 71:46–73:14 · 대본 220단어 · 별도 활동 0초

진행 메모: [버퍼] 체크포인트 ④ 대기용. 요일 시나리오가 현실 드리프트의 축소판임을 정당화.

Distribution change can originate in ordinary operational work. An application update can change a fingerprint. A proxy rollout can alter the relationship between observed addresses and users. A workload cycle can change the mix of flows. Attackers can also change their behavior, but they are not the only source of unfamiliar traffic.

This matters because a monitoring signal does not name its own cause. Suppose the predicted-attack rate drops. Perhaps the environment is quieter. Perhaps the model is missing a new attack family. Perhaps preprocessing stopped producing a useful feature. The same direction of change can support several hypotheses.

A practical investigation should therefore compare model telemetry with operational context. What changed in the infrastructure? Did the collection pipeline change? Is the shift concentrated in one service, sensor, or traffic category? Those questions can make a broad warning much more actionable.

Our traffic lab compresses several differences into daily slices. That makes a clear teaching example, but we should avoid treating Friday as a universal model of all drift. The measured result belongs to that configuration and dataset.

The general habit is to preserve alternatives while collecting evidence. We can restrict an affected automated action before knowing the complete cause, provided the policy defines that response. We should then investigate systematically instead of immediately assuming that retraining is the solution.

### 47. The drift-detection toolbox

진행 73:14–74:43 · 대본 222단어 · 별도 활동 0초

진행 메모: "도구가 없어서가 아니라 알람에 안 물려놔서 놓친다." 데모3의 rate 신호를 표의 2·3행과 연결.

The monitoring toolbox contains observations at several levels. Input-distribution checks examine features. Prediction-rate monitors examine the mix of model outputs. Acceptance-rate monitors examine the fraction passing a policy. Stream methods look for changes in a chosen sequence. Delayed-label audits measure outcomes once ground truth becomes available.

The choice of window and comparison group is part of the monitor. A nightly backup pattern may look unusual against an all-day baseline while being ordinary compared with previous backup periods. A global average may hide a serious change affecting one service.

For an operational design, I would specify the reference period, minimum sample size, grouping, and the response to a trigger. Without those details, saying that we monitor drift is difficult to evaluate. A dashboard is not yet an investigation procedure.

Also distinguish a statistically detectable change from a harmful change. With large volumes, small differences may be easy to detect. Their operational significance depends on the action and supporting evidence. Repeated alerts that nobody can interpret can consume the capacity intended for real investigations.

Demo Three focuses on simple predicted-attack and acceptance rates. We will observe that they move. We are not evaluating a complete alarm threshold or proving its false-alarm performance. That would require a separate study over relevant stable and changing periods. Today, the rates help us identify a reason to investigate.

### 48. Demo 3 — a real collapse, in real silence

진행 74:43–76:45 · 대본 230단어 · 별도 활동 30초

진행 메모: "운영엔 라벨이 없다 = acc 행은 가려져 있다고 상상하라. 평균은 침묵, 레이트가 비명." Lab1과의 대비(합의도 침묵!)를 강조 → Part 4로.

Read the accuracy row first, using the reference values as our guide. Baseline accuracy is about ninety-six point one percent on the holdout and sixty-eight point six percent on Friday. That is a substantial difference across these evaluation slices.

Now look at mean confidence. It is about zero point nine one six on the holdout and zero point nine one three on Friday. Mean agreement is also close: approximately zero point nine six nine and zero point nine six eight. Those averages do not provide an obvious warning proportional to the accuracy decline.

The rate rows change more visibly. The predicted-attack rate moves from about twenty-one point seven percent to eleven point two percent. The accepted-attack rate moves from about thirteen point nine percent to seven point nine percent. These are observations about the model's outputs and gate, not measurements of the true attack prevalence.

The reference also contains one thousand two hundred fifty-eight Friday predictions that are wrong while carrying baseline confidence at least zero point nine. That count requires labels. It helps us evaluate the failure afterward, but an operator would not know that count immediately.

This result limits our interpretation of Lab One. Agreement can be useful against one constructed mechanism and remain high in another failure setting. We need to inspect multiple signals and design a response that does not treat unanimity as proof of correctness.

[읽지 않음 / 별도 활동] Read the live or clearly identified reference result.

### 49. Friday, before the labels arrive

진행 76:45–79:41 · 대본 217단어 · 별도 활동 90초

진행 메모: 90초 동안 정확도 수치를 근거로 쓰지 않고 관측 가능한 신호만으로 대응을 정한다. 정답은 대본에서 토의 후 공개.

Now imagine the labels have not arrived. I have removed the accuracy row and the high-confidence error count. What remains is exactly the kind of information we could observe from model outputs: confidence, agreement, predicted-attack rate, and accepted-attack rate.

Please decide what you would investigate and which automated actions, if any, you would restrict. Work from the visible evidence. Do not justify your decision using the accuracy decline we already know from the offline experiment. That information is unavailable in this scenario.

[읽지 않음: 여기서 90초 활동. Individual or pair discussion using only label-free signals.]

One defensible response is to investigate the changed rates while temporarily limiting consequential automation in the affected traffic slice. We would inspect preprocessing, compare traffic categories, check recent changes, and collect a sample for labeling. The appropriate restriction depends on the existing response policy and the cost of delaying action.

It would be too strong to conclude that the lower predicted-attack rate proves fewer attacks. It would also be too strong to conclude that it proves model failure. We have a change that needs an explanation.

The high mean agreement does not cancel that need. Multiple signals can disagree about how reassuring the situation looks. A useful policy specifies what happens when they do. Our next section turns that principle into explicit routes for individual outputs and broader restrictions when monitoring indicates a possible change.

[읽지 않음 / 별도 활동] Individual or pair discussion using only label-free signals.

### 50. Accept / Review / Withhold

진행 79:41–81:11 · 대본 224단어 · 별도 활동 0초

진행 메모: 청중이 가져갈 1장. 임계값은 예시일 뿐, 자기 트래픽으로 튜닝하라 강조.

We now connect the evidence to action. Accept means that a prediction is eligible for the action allowed by a validated policy. Review means that a person or an additional verification process needs to inspect it. Withhold means that the proposed automated action should not proceed under the current evidence.

Those routes do not directly mean attack, uncertain attack, and benign. They describe what the system is allowed to do. An attack prediction can be withheld because the evidence is incomplete. A prediction sent for review can later be confirmed and acted upon.

The acceptance condition needs more than high agreement. We have just seen why. It should include the validated threshold, relevant evidence checks, and the health of the monitoring context. The permitted action also matters. A policy suitable for adding an annotation may be insufficient for blocking production traffic.

Review needs an owner, a useful evidence bundle, and an expected response time. Withholding needs a next step, such as collecting missing records or escalating an affected slice. Otherwise these categories merely rename unresolved work.

For the lab, we can illustrate a threshold. For deployment, the team needs to validate the complete policy on representative data and make its limits explicit. The route should explain why an action was allowed or delayed, so a later audit can reconstruct the decision and improve it.

### 51. Signal → action map

진행 81:11–82:40 · 대본 222단어 · 별도 활동 0초

진행 메모: 4행 모두 오늘 데모에서 실제로 본 패턴과 연결해 설명.

This table maps observed patterns to investigations and actions. High confidence with low agreement suggests that the summaries are in tension. It can motivate review, but it does not identify shortcut use or evasion as the unique cause.

High and stable agreement also needs context. The CIC result showed that average agreement can stay high through a serious performance difference. Before accepting an output, we still need policy eligibility and the required evidence checks.

If agreement declines across a traffic group, we can investigate a distribution or pipeline change. We should not automatically retrain on the next batch without establishing its quality and labels. Retraining can preserve or introduce a problem if the diagnosis is wrong.

The final row reflects the actual CIC pattern: stable means alongside changing predicted-attack and acceptance rates. That pattern justifies investigation and, where the policy requires it, restriction of affected automation. It does not supply a complete incident diagnosis.

The map is therefore a starting point for a runbook. A production version should name the responsible team, the records to inspect, and the condition for restoring the action. The restoration condition is especially important. Freezing automation is easy to describe. Resuming it responsibly requires evidence that the relevant problem has been understood or the policy has been revalidated. We will now practice choosing routes with incomplete information.

### 52. Choose a route and name the evidence

진행 82:40–86:05 · 대본 213단어 · 별도 활동 120초

진행 메모: 90초 개인 판단 후 30초 손들기. 예시 답은 A 조건부 accept, B review, C 영향 구간 자동조치 withhold와 조사. 조직 정책에 따른 근거 있는 대안을 허용한다.

Here are three hypothetical alerts. For each one, choose accept, review, or withhold, and name the evidence that supports your choice. Assume acceptance requires a previously validated policy and healthy monitoring. The examples are a decision exercise, not new measurements from the lab.

[읽지 않음: 여기서 120초 활동. 90 seconds to choose routes, then 30 seconds for a show of hands.]

Alert A has high agreement, matching raw logs, and normal traffic trends. Conditional acceptance may be reasonable if it is within the validated policy and the allowed action has the appropriate scope. High agreement alone would not be enough.

Alert B has high confidence, disagreement among experts, and incomplete logs. Review is a reasonable route because the confidence does not resolve the conflicting or missing evidence. The next step is to obtain the relevant records and inspect the disagreement.

Alert C has high agreement but an abrupt acceptance-rate change of unknown cause. Withholding consequential automation in the affected context while investigating is defensible. The observation could have a legitimate explanation, so the response should remain tied to scope and policy.

Different organizations can justify different actions if they state the costs and evidence requirements. The exercise is successful when you can explain what would change your decision. For example, a verified pipeline issue, a validated traffic change, or additional raw evidence might support a different route on the next review.

[읽지 않음 / 별도 활동] 90 seconds to choose routes, then 30 seconds for a show of hands.

### 53. When the AI in your SOC is an LLM

진행 86:05–87:33 · 대본 221단어 · 별도 활동 0초

진행 메모: 유창함 ≠ 정확함. "오늘 배운 원칙이 그대로 이식된다"가 요지.

The same questions apply when a security workflow uses a language model. Suppose it drafts an incident summary, enriches an alert, or proposes an investigation query. A polished explanation can make the result feel reliable even when an important claim lacks evidence.

We should avoid assuming that a verbal confidence statement has a calibrated interpretation. The phrase I am quite sure does not, by itself, identify an evaluated probability. We need task-specific verification of the actual claim.

For an incident summary, that might mean linking each material assertion to a log record with the right timestamp and entity. For a proposed query, we can inspect the query and its returned records. For a suggested action, we can check scope and policy eligibility before execution.

There are limits to the analogy with classifiers. A free-form answer may contain several claims, each with a different evidential status. One scalar score can hide that structure. The verification unit may need to be the individual claim or proposed operation rather than the complete response.

The common operational principle is to make the output inspectable. Ask what was observed, what was inferred, and which evidence could overturn the inference. Then route the proposed action through an appropriate verification process. Fluent language can help communicate the analysis, but it does not remove the need to check it.

### 54. Trusting (the work of) agents

진행 87:33–89:01 · 대본 219단어 · 별도 활동 0초

진행 메모: 회수 문장의 정식 버전. take-home 전에 미리 한 번 심는 것.

Think back to how we used an agent during the demonstrations. We gave it a bounded task, supplied the expected verification, and inspected the result. That is a practical example of evaluating completed work rather than accepting a confident description of work.

An independent check can help, but independence deserves the same scrutiny we applied to ensembles. Two agents using the same incorrect source may agree. Repeating a calculation with a tool or checking the original record can provide a different kind of evidence than asking another model for its opinion.

Autonomy should also depend on the action. A workflow might allow an agent to draft an explanation freely, require a check before changing a configuration, and apply additional restrictions before a consequential operation. The specific tiers come from the organization's policy and measured experience.

For monitoring, track observable outcomes: failed tasks, required corrections, and changes in the kinds of work being attempted. Counts and denominators matter here too. A lower failure count may simply reflect fewer tasks or a different task mix.

Finally, preserve enough information to reconstruct a decision. What input did the agent receive? What did it do? Which check passed? That record makes trust something we can examine and revise. It is the same reason we pinned configurations and inspected reference comparisons in the laboratory.

### 55. Tune the gate on your own numbers

진행 89:01–90:31 · 대본 226단어 · 별도 활동 0초

진행 메모: 라이브로 안 돌림(시간). "이 게이트를 여러분 트래픽으로 튜닝하는 것이 숙제."

This take-home prompt asks you to explore the acceptance threshold on your own outputs. It requests a policy table for several precision targets, including the threshold, coverage, and true- and false-positive counts. Those quantities let you inspect the tradeoff instead of choosing a threshold because it looks familiar.

Treat the sweep as exploratory analysis. If you use the same labels to select and report the threshold, describe the resulting table as a validation or exploration result. Freeze the policy and evaluate it on untouched data before presenting it as a deployment estimate.

The prompt writes a new experiment file and preserves the frozen configuration. That separation helps keep the original tutorial reproducible while allowing additional analysis. It also makes it clearer which result belongs to the reference demonstration and which belongs to your extension.

When applying the idea to your own traffic, add the operational questions we discussed. What happens to rejected predictions? How large is the review queue? Which actions are allowed for accepted outputs? A precision target without those details does not define a complete policy.

We will not run this sweep during the session. The useful next step is to choose a relevant dataset and establish the split roles before experimenting. That gives the resulting table a clear interpretation and avoids quietly using the final evaluation set to choose the most attractive threshold.

### 56. Deployment checklist

진행 90:31–92:00 · 대본 221단어 · 별도 활동 0초

진행 메모: 체크리스트 낭독은 빠르게. 마지막 항목이 아티팩트/재현성 철학 연결.

Here is a deployment checklist to connect the technical observations with implementation. First, assess calibration on suitable labeled data and record what population the assessment covers. A past result should have a date, dataset, and procedure behind it.

Second, define the abstention path before enabling an automated action. Decide who receives a reviewed case, what evidence accompanies it, and what happens if the queue exceeds capacity. A gate cannot take responsibility for those downstream decisions by itself.

Third, emit the telemetry required to investigate changes. That includes the selected scores and the context needed to aggregate them meaningfully. A single global average may hide the traffic group that needs attention.

Fourth, connect monitoring to a response. Name the owner, the investigation steps, and the condition for restricting or restoring the action. Otherwise a dashboard can show a problem without changing what the system does.

Finally, preserve the information needed to reproduce the policy: environment, data processing, model, threshold, and expected checks. Reproduction does not prove operational validity, but it lets us determine what was actually evaluated.

If I had to choose where to start, I would identify one consequential automated action and document its evidence requirement and fallback. That creates a concrete place to apply the calibration, selection, and monitoring measurements, rather than collecting metrics with no decision attached to them.

### 57. What today's lab does not prove

진행 92:00–93:31 · 대본 228단어 · 별도 활동 0초

진행 메모: 한계를 먼저 말하면 질문 절반이 사라진다. 4번째 불릿이 VALIDS류 연구 필요성으로 연결되는 다리.

Let us state the limits of today's evidence. The synthetic lab deliberately constructs a failure mechanism. It demonstrates that confident errors can occur and that a particular diversity design can help in that setting. Its error rates are not estimates for a production network.

The traffic lab uses one dataset and a specific temporal split. It shows that the baseline's measured performance can differ substantially while mean confidence and mean agreement remain high. It does not establish a universal drift detector or isolate one cause of that difference.

The threshold results also have selection limits. Demo Two explores thresholds on the labeled evaluation sample. Demo Three selects on the earlier holdout before applying the policy to later slices. Those roles must remain visible when we describe precision and transfer.

We introduced evidence tests as an operational design idea, with a hypothetical flow example. We did not measure a full evidence-verification architecture in the three demonstrations. Likewise, a reference-matching run verifies reproduction within the stated tolerance, rather than proving that a model is suitable for every deployment.

These limits tell us what to do next. Evaluate a frozen policy on relevant untouched data, inspect the accepted and rejected populations, and test monitoring responses over time. The lab gives us questions, mechanisms, and a reproducible starting point. The deployment decision needs evidence from the environment where the action will occur.

### 58. The whole story, on one screen

진행 93:31–96:34 · 대본 232단어 · 별도 활동 90초

진행 메모: D 키로 대시보드 전환. 대본 발화와 별도 조작 90초를 합쳐 진행한다.

Let us return to the dashboard and connect the experiments. Start with Demo One. The baseline's confidence is higher among its mistakes, while agreement decreases among the ensemble's mistakes. This teaches us to evaluate a score's relationship with correctness rather than infer it from the score's name.

Now move to Demo Two. The ensemble-and-agreement configuration retains far more true attack alerts under the sample's strict precision criterion. Check the counts as well as the percentages. Remember that the threshold search uses those labels, so the result illustrates selective potential rather than independently validating a production cutoff.

Finally, inspect the CIC drift experiment. The reassuring average scores survive a large difference in baseline accuracy. The prediction and acceptance rates move. This teaches us to watch behavior over populations and time, while keeping the cause of a change open to investigation.

I will give you a moment to read the values on each card. Check whether the dashboard identifies live outputs or reference data, and compare it with the verification reports. If a card is incomplete, we should acknowledge that rather than fill in a success claim verbally.

The combined interpretation is more useful than any single favorable result. A signal can help, a gate can retain a useful subset, and both can require renewed scrutiny when the evaluation context changes. That is why the operational policy includes evidence checks, review, and monitoring together.

[읽지 않음 / 별도 활동] Navigate dashboard cards and allow the audience to inspect values; narration is counted separately.

### 59. Three ways to break the lab (please do)

진행 96:34–98:18 · 대본 223단어 · 별도 활동 15초

진행 메모: "깨뜨려 보라"가 최고의 숙제. 프롬프트 3종은 리포에 준비되어 있음.

Here are three ways to extend the laboratory after the session. You can make the evasive test condition stronger, change the ensemble so more experts see the shortcut, or bring another detector and evaluate its confidence on the same examples.

Before running an extension, write down a prediction. If every expert sees the shortcut, do you expect the disagreement signal to become more informative or less informative? If you strengthen evasion, which metric should change first in your proposed explanation? The point is to test a mechanism rather than collect another attractive number.

Keep the original configuration and reference outputs intact. Put exploratory changes in a separate experiment, report what differs, and preserve the resulting inputs and outputs. That lets another person reproduce both the original demonstration and your extension.

Also consider a negative result. If your prediction fails, that can teach us that the proposed explanation was incomplete. Do not treat agreement with an expected narrative as the only successful outcome.

Please choose one extension that connects with your own work. It might be a different traffic slice, a different evidence subset, or a more realistic acceptance policy. Start with a bounded question and a measurable outcome. The repository provides a shared starting point, but the most valuable extension is the one that tests an assumption your own operational decision depends on.

[읽지 않음 / 별도 활동] Audience chooses one take-home experiment.

### 60. Take-home

진행 98:18–100:00 · 대본 217단어 · 별도 활동 15초

진행 메모: 회수 문장 → QR → "질문은 세션 끝나고 개별로." QR 안내 후 마무리.

We began with a model that was more confident when it was wrong. That result challenged the assumption that a strong score is enough to justify action. We then examined calibration, agreement, and selective acceptance, and saw both their usefulness and their limits.

The first practical takeaway is to connect evaluation to the decision. State which outputs can trigger which actions, and report the counts and denominators that describe the policy. An impressive accuracy or precision value without that context leaves the operational question unanswered.

The second takeaway is to make uncertainty actionable. Review and withholding need owners and next steps. High agreement needs evidence and a healthy monitoring context. A changed rate needs investigation rather than an automatic story about its cause.

The final takeaway is to verify the work. That applies to a detector, an explanation, an agent, and the experimental pipeline itself. Preserve enough evidence to distinguish a reproduced result from a confident claim, and enough evaluation discipline to distinguish a laboratory result from a deployment guarantee.

The QR code links to the artifact and prompts so you can revisit the experiments. Thank you for working through the examples and decisions with me. I would be happy to discuss how these checks could fit your own traffic, model, or response workflow after the session.

[읽지 않음 / 별도 활동] Allow time to scan the QR code.

## 근거 및 계산 범위

- 데모 수치: expected_outputs/demo1.json, demo2.json, demo3_cic.json. 대본의 수치는 고정 기준값이며 실제 실행 결과가 다르면 화면 값과 검증 결과를 우선합니다.
- 평가 절차: experiments/demo2_selective.py, experiments/demo3_cic_drift.py, src/common.py, src/config_cic.py.
- Calibration: [Guo et al., 2017](https://proceedings.mlr.press/v70/guo17a.html).
- Conformal prediction: [Angelopoulos and Bates, 2022](https://arxiv.org/abs/2107.07511).
- 오탐 비용, confidence bin, 투표 수, 운영 대응 사례는 개념 설명용 가상 예시입니다.
- 단어 수는 영문·숫자 토큰 기준이며 축약형·소수·하이픈 단어를 한 단어로 셉니다. 수치를 길게 발음하거나 약어를 철자별로 읽으면 더 걸릴 수 있습니다. 부록·진행 메모·활동 표식은 제외했습니다.
